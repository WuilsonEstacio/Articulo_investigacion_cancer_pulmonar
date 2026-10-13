"""Vector polygon centerline extraction; no clinical target enters calibration."""
import numpy as np
import pandas as pd
import pymupdf


def horizontal_edges(segments):
    """Coalesce collinear fragments, retaining contour direction and provenance.

    PDF coordinates are rounded to 0.001 pt; this is a geometric precision
    allowance, not a clinical tolerance or a minimum plateau length.
    """
    edges={1:[], -1:[]}
    for sign in edges:
        parts=sorted([(min(a[0],b[0]),max(a[0],b[0]),(a[1]+b[1])/2,j)
                      for j,a,b in segments
                      if abs(a[1]-b[1])<=.002 and (b[0]-a[0])*sign>1e-6],
                     key=lambda v:(v[2],v[0]))
        for left,right,y,j in parts:
            if edges[sign] and abs(y-edges[sign][-1]['y'])<=.002:
                last=edges[sign][-1]
                if left>last['right']+.002 or right<last['left']-.002:
                    raise ValueError('Disconnected horizontal fragments at one level')
                last['left']=min(left,last['left'])
                last['right']=max(right,last['right'])
                last['segments'].append(j)
            else:
                edges[sign].append(dict(left=left,right=right,y=y,segments=[j]))
    return edges


def polygon_plateaus(segments, width=.502):
    """Pair opposite horizontal edges even when the vertical slice is thick.

    Short plateaus may have *no overlap* between their two offset edges.
    The lower left and upper right corners still identify the central span.
    Opposite-direction 0.251-pt join artefacts do not form width-sized pairs.
    """
    edges=horizontal_edges(segments)
    pairs=[]
    used=set()
    for upper in edges[1]:
        matches=[(i,lower) for i,lower in enumerate(edges[-1])
                 if abs(lower['y']-upper['y']-width)<=.0021
                 and -.003<=upper['left']-lower['left']<=width+.003
                 and -.003<=upper['right']-lower['right']<=width+.003]
        if len(matches)>1:
            raise ValueError('Ambiguous horizontal edge pairing')
        if not matches:
            continue
        i,lower=matches[0]
        if i in used:
            raise ValueError('Reused horizontal edge')
        used.add(i)
        half=(lower['y']-upper['y'])/2
        pairs.append(dict(left=lower['left']+half,right=upper['right']-half,
                          y=(upper['y']+lower['y'])/2,
                          upper_segments=','.join(map(str,upper['segments'])),
                          lower_segments=','.join(map(str,lower['segments'])),
                          edge_separation=2*half))
    if not pairs:
        raise ValueError('No paired horizontal edges')
    # Butt end caps are not shifted along x.
    pairs[0]['left']=min(a[0] for _,a,b in segments)
    pairs[-1]['right']=max(a[0] for _,a,b in segments)
    for a,b in zip(pairs,pairs[1:]):
        if abs(a['right']-b['left'])>.004:
            raise ValueError('Unrecovered plateau or noncontiguous centerline')
    for p in pairs:
        if p['right']<p['left']:
            if p['left']-p['right']>.002:
                raise ValueError('Negative plateau extent')
            # Near-coincident events can be closer than PDF float precision.
            # Keep the level, collapsing only its unresolvable horizontal span.
            p['left']=p['right']=(p['left']+p['right'])/2
    return pairs


def extract_pdf(pdf, config, output):
    doc = pymupdf.open(pdf)
    curves, audit = {}, {}
    for endpoint, page_num in config['pages'].items():
        page = doc[page_num - 1]
        words = page.get_text('words')
        xt = [w for w in words if w[4].isdigit() and 193 < w[1] < 197 and 80 < w[0] < 350]
        yt = [w for w in words if w[4].isdigit() and w[2] < 82 and 65 < w[1] < 195]
        assert len(xt) == 22 and len(yt) == 11, (endpoint, len(xt), len(yt))
        ax, bx = np.polyfit([int(w[4]) for w in xt], [(w[0]+w[2])/2 for w in xt], 1)
        ay, by = np.polyfit([int(w[4])/100 for w in yt], [(w[1]+w[3])/2 for w in yt], 1)
        draws = page.get_drawings()
        risk_rows = []
        for arm, color in config['colors'].items():
            ids = [i for i,d in enumerate(draws) if d['fill'] and np.linalg.norm(np.array(d['fill'])-color)<config['color_tolerance'] and d['rect'].y1<195]
            candidates = [i for i in ids if draws[i]['rect'].width>200 and len(draws[i]['items'])>100]
            chosen = min(candidates, key=lambda i:len(draws[i]['items']))
            segments = [(j, tuple(it[1]), tuple(it[2])) for j,it in enumerate(draws[chosen]['items']) if it[0]=='l']
            pd.DataFrame([dict(page=page_num,path_id=chosen,segment=j,x1=a[0],y1=a[1],x2=b[0],y2=b[1]) for j,a,b in segments]).to_csv(output/f'segments_{endpoint}_{arm}.csv',index=False)
            paired=polygon_plateaus(segments)
            pd.DataFrame(paired).assign(page=page_num,path_id=chosen).to_csv(output/f'plateaus_{endpoint}_{arm}.csv',index=False)
            plateaus=[(p['left'],p['right'],p['y']) for p in paired]
            first_y=plateaus[0][2]
            rows=[]
            for k,(l,r,y) in enumerate(plateaus):
                x=bx if k==0 else (plateaus[k-1][1]+l)/2
                rows.append(dict(page=page_num,path_id=chosen,x_pdf=x,y_pdf=y,time_months=max(0,(x-bx)/ax),survival=1+(y-first_y)/ay,kind='plateau'))
            end=plateaus[-1][1]
            rows.append(dict(page=page_num,path_id=chosen,x_pdf=end,y_pdf=plateaus[-1][2],time_months=(end-bx)/ax,survival=rows[-1]['survival'],kind='support_end'))
            points=pd.DataFrame(rows)
            if (np.diff(points.survival)>2e-5).any():
                raise ValueError(f'Nonmonotone vector extraction: {endpoint} {arm}')
            points['survival']=np.minimum.accumulate(points.survival)
            points.to_csv(output/f'points_{endpoint}_{arm}.csv',index=False)
            curves[endpoint,arm]=points
            markers=[]
            seen=set()
            for i in ids:
                rect=draws[i]['rect']
                if len(draws[i]['items'])==1 and rect.width<1 and 3<rect.height<7:
                    key=tuple(round(v,2) for v in rect)
                    if key in seen:
                        continue
                    seen.add(key)
                    markers.append(dict(page=page_num,path_id=i,x_pdf=(rect.x0+rect.x1)/2,y_pdf=(rect.y0+rect.y1)/2,time_months=((rect.x0+rect.x1)/2-bx)/ax,survival=1+((rect.y0+rect.y1)/2-first_y)/ay))
            pd.DataFrame(markers).to_csv(output/f'censor_marks_{endpoint}_{arm}.csv',index=False)
            label=[w for w in words if w[4].lower()==arm and 220<w[1]<245][0]
            nums=sorted([w for w in words if w[4].isdigit() and abs(w[1]-label[1])<0.1 and 78<w[0]<350],key=lambda w:w[0])
            assert len(nums)==22
            for t,w in zip(range(0,64,3),nums):
                risk_rows.append(dict(endpoint=endpoint,arm=arm,time_months=t,at_risk=int(w[4]),page=page_num,x_pdf=(w[0]+w[2])/2,y_pdf=(w[1]+w[3])/2))
            audit[f'{endpoint}_{arm}']=dict(page=page_num,path_id=chosen,other_path_ids=candidates,x_scale=ax,x_origin=bx,y_scale=ay,y_text_origin=by,first_y=first_y,origin_shift_probability=1-(first_y-by)/ay,points=len(points),support_end=float(points.time_months.iloc[-1]),unique_marks=len(markers),monotone=True,s0=float(points.survival.iloc[0]))
            audit[f'{endpoint}_{arm}']['paired_horizontal_levels']=len(paired)
        pd.DataFrame(risk_rows).to_csv(output/f'risk_pdf_{endpoint}.csv',index=False)
    doc.close()
    return curves,audit