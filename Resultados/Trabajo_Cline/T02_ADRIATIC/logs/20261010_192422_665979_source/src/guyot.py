"""Independent bounded implementation of Guyot 2012 equations 1-9.

No fitting to published medians, landmarks or hazard ratios.
"""
import numpy as np
import pandas as pd


def step_at(times, survival, query):
    times, survival = np.asarray(times), np.asarray(survival)
    ix = np.searchsorted(times, query, side='right')-1
    return np.where(ix>=0, survival[np.maximum(ix,0)], 1.0)


def _interval(t, s, start, end, n, initial_s, ncensor):
    ct=start+np.arange(1,ncensor+1)*(end-start)/(ncensor+1)
    risk=int(n)
    shat=float(initial_s)
    cursor=0
    records=[]
    error=0.0
    for tk,sk in zip(t,s):
        while cursor<len(ct) and ct[cursor]<tk:
            if risk<=0:
                return None
            records.append((ct[cursor],0))
            risk-=1
            cursor+=1
        dk=int(np.rint(risk*(1-sk/shat))) if shat>0 and risk>0 else 0
        dk=min(risk,max(0,dk))
        if dk:
            shat*=1-dk/risk
            records.extend([(tk,1)]*dk)
            risk-=dk
        error+=(shat-sk)**2
    while cursor<len(ct):
        if risk<=0:
            return None
        records.append((ct[cursor],0))
        risk-=1
        cursor+=1
    return records,risk,shat,error


def reconstruct(times, survival, risk_times, risks, total_events):
    t=np.asarray(times,dtype=float)
    s=np.asarray(survival,dtype=float)
    rt=np.asarray(risk_times,dtype=float)
    nr=np.asarray(risks,dtype=int)
    if len(t)!=len(s) or len(t)<2 or np.any(np.diff(t)<0) or np.any(np.diff(s)>1e-9):
        raise ValueError('Invalid curve')
    if t[0]!=0 or abs(s[0]-1)>1e-9 or np.any(s<0) or np.any(s>1):
        raise ValueError('Invalid probability/origin')
    if len(rt)!=len(nr) or rt[0]!=0 or np.any(np.diff(rt)<=0) or np.any(np.diff(nr)>0) or np.any(nr<0):
        raise ValueError('Invalid risk table')
    if not 0<=total_events<=nr[0]:
        raise ValueError('Invalid total events')
    augmented=np.unique(np.r_[t,rt[rt<=t[-1]]])
    s=step_at(t,s,augmented)
    t=augmented
    end_support=t[-1]
    last=int(np.where((rt<end_support)&(nr>0))[0][-1])
    records=[]
    audit=[]
    n=int(nr[0])
    shat=1.0
    for i in range(last+1):
        a=rt[i]
        b=min(rt[i+1] if i+1<len(rt) else end_support,end_support)
        final=i==last
        mask=(t>=a)&((t<=b) if final else (t<b))
        ti=t[mask]
        si=s[mask]
        target=int(nr[i+1]) if i+1<len(nr) and rt[i+1]<=end_support else 0
        best=None
        previous_events=sum(e for _,e in records)
        for nc in range(n+1):
            cand=_interval(ti,si,a,b,n,shat,nc)
            if cand is None:
                continue
            rec,remain,ss,error=cand
            de=sum(e for _,e in rec)
            # Final survivors are administratively censored at the plotted endpoint.
            risk_error=0 if final and target==0 else abs(remain-target)
            key=(risk_error,abs(previous_events+de-total_events) if final else 0,error,nc)
            if best is None or key<best[0]:
                best=(key,cand,nc)
        if best is None:
            raise RuntimeError('No feasible integer reconstruction')
        key,(rec,remain,ss,error),nc=best
        if final:
            rec.extend([(end_support,0)]*remain)
            remain=0
        audit.append(dict(interval=i,start=a,end=b,input_risk=int(nr[i]),actual_start=n,target_end=target,actual_end=remain,events=sum(e for _,e in rec),censors=sum(1-e for _,e in rec),uniform_censors=nc,squared_error=error,total_event_gap_after=sum(e for _,e in records+rec)-total_events))
        records.extend(rec)
        n=remain
        shat=ss
    ipd=pd.DataFrame(records,columns=['time_months','event']).sort_values(['time_months','event'],ascending=[True,False]).reset_index(drop=True)
    if len(ipd)!=nr[0] or (ipd.time_months>end_support+1e-9).any():
        raise RuntimeError('Population conservation/support violation')
    return ipd,pd.DataFrame(audit)