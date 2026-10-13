"""E2.0b: vector PDF rendering independent of the extraction inverse."""
from pathlib import Path
import numpy as np
import pymupdf
from lifelines import KaplanMeierFitter


class FigureGeometry:
    def __init__(self,cfg):
        with pymupdf.open(Path(cfg['project_root'])/cfg['pdf_relative']) as doc:
            page=doc[cfg['pages']['SG']-1]
            self.size=(page.rect.width,page.rect.height)
            words=page.get_text('words')
            self.xt=[w for w in words if w[4].isdigit() and 193<w[1]<197 and 80<w[0]<350]
            self.yt=[w for w in words if w[4].isdigit() and w[2]<82 and 65<w[1]<195]
            self.ax,self.bx=np.polyfit([int(w[4]) for w in self.xt],[(w[0]+w[2])/2 for w in self.xt],1)
            self.ay,_=np.polyfit([int(w[4])/100 for w in self.yt],[(w[1]+w[3])/2 for w in self.yt],1)
            draws=page.get_drawings()
            color=cfg['colors']['durvalumab']
            candidates=[d for d in draws if d['fill'] and np.linalg.norm(np.array(d['fill'])-color)<cfg['color_tolerance'] and d['rect'].y1<195 and d['rect'].width>200 and len(d['items'])>100]
            chosen=min(candidates,key=lambda d:len(d['items']))
            self.y0=chosen['rect'].y0+.502/2
            self.labels={arm:next(w for w in words if w[4].lower()==arm and 220<w[1]<245) for arm in cfg['colors']}
            self.risk={arm:sorted([w for w in words if w[4].isdigit() and abs(w[1]-label[1])<.1 and 78<w[0]<350],key=lambda w:w[0]) for arm,label in self.labels.items()}

    @staticmethod
    def text(page,word,value):
        # Preserve the template text bounding-box center and height. Font glyph
        # widths may differ: calibration is performed again on the saved PDF.
        font=pymupdf.Font('helv')
        size=(word[3]-word[1])/(font.ascender-font.descender)
        width=font.text_length(str(value),fontsize=size)
        x=(word[0]+word[2]-width)/2
        baseline=word[1]+font.ascender*size
        page.insert_text((x,baseline),str(value),fontsize=size,fontname='helv')

    def render(self,path,pair,cfg):
        doc=pymupdf.open()
        page=doc.new_page(width=self.size[0],height=self.size[1])
        for word in self.xt+self.yt:
            self.text(page,word,word[4])
        half=.502/2
        for arm,truth in pair.items():
            km=KaplanMeierFitter().fit(truth.time_months,truth.event)
            sf=km.survival_function_.iloc[:,0]
            change=np.r_[True,np.diff(sf.to_numpy())<0]
            ts=sf.index.to_numpy()[change]
            ys=self.y0+self.ay*(sf.to_numpy()[change]-1)
            xs=self.bx+self.ax*ts
            end=self.bx+self.ax*float(truth.time_months.max())
            upper=[]
            lower=[]
            for i,y in enumerate(ys):
                left=xs[i]
                right=xs[i+1] if i+1<len(xs) else end
                upper.extend([(left+(half if i else 0),y-half),(right+(half if i+1<len(xs) else 0),y-half)])
                lower.extend([(left-(half if i else 0),y+half),(right-(half if i+1<len(xs) else 0),y+half)])
            polygon=upper+list(reversed(lower))
            shape=page.new_shape()
            shape.draw_polyline(polygon)
            shape.finish(color=None,fill=cfg['colors'][arm],closePath=True)
            shape.commit()
            for time in truth.loc[truth.event==0,'time_months']:
                x=self.bx+self.ax*time
                y=self.y0+self.ay*(float(km.predict(time))-1)
                page.draw_rect(pymupdf.Rect(x-half,y-2.5,x+half,y+2.5),color=None,fill=cfg['colors'][arm])
            self.text(page,self.labels[arm],arm)
            for t,word in zip(range(0,64,3),self.risk[arm]):
                self.text(page,word,int((truth.time_months>=t).sum()))
        # Suppress random document IDs for byte-for-byte replay.
        doc.save(path,deflate=True,no_new_id=True)
        doc.close()