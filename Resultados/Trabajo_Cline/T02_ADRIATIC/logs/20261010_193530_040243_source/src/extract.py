"""Vector polygon centerline extraction; no clinical target enters calibration."""
import numpy as np
import pandas as pd
import pymupdf


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
            xs = sorted(set(p[0] for _,a,b in segments for p in [a,b]))
            plateaus=[]
            for left,right in zip(xs[:-1],xs[1:]):
                if right-left<1e-5:
                    continue
                x=(left+right)/2
                ys=[a[1]+(x-a[0])*(b[1]-a[1])/(b[0]-a[0]) for _,a,b in segments if min(a[0],b[0])<x<max(a[0],b[0])]
                if len(ys)<2 or max(ys)-min(ys) > 0.55:
                    continue
                y=(max(ys)+min(ys))/2
                if plateaus and abs(y-plateaus[-1][2])<0.002:
                    plateaus[-1][1]=right
                else:
                    plateaus.append([left,right,y])
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
        pd.DataFrame(risk_rows).to_csv(output/f'risk_pdf_{endpoint}.csv',index=False)
    return curves,audit