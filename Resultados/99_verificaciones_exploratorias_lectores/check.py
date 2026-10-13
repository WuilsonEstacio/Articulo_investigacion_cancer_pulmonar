import numpy as np
# LQ Table 6
a,b=0.35,0.035
for D in [5,10,15,20]: print(D, round(1-np.exp(-(a*D+b*D*D)),3))
# Vasculature Thiele
R,Dg,rV,lam,P=100,0.396,0.25,7.6e-10,1e9
p2=np.sqrt(R**2/Dg*rV); p1=np.sqrt(R**2/Dg*(lam*P+rV)); print('phi',p1,p2,'c_inf',p2**2/p1**2)
for q1 in [160,126,105]: print(q1,(80/q1)**2)
# Td from Fig A2
print('Td', 98*np.log(2)/np.log(5.5/4.5))
# eq diam
V=0.908; print('cube',V**(1/3),'sphere',(6*V/np.pi)**(1/3))
# combo CKR
print(1-(1-0.28)*(1-0.4))
# Appendix A example NSCLC
Tp=70.; am=np.log(2)/Tp
Tc,TG0,PG=50.,150.,0.1
Ps=(1-np.exp(am*Tc)/2)/(1-(PG/TG0)/(am+1/TG0)); print('Psleep',Ps)
Td=370*24; ag=np.log(2)/Td; RA=0.0005
Psym=np.exp((ag+RA)*Tc)/(1-Ps+Ps*(PG/TG0)/(ag+RA+1/TG0))-1; print('Psym',Psym)
GF=0.23;RAD=0.005
A=(ag+RA)/(np.exp((ag+RA)*Tc)-1); B=(1-Psym)/(ag+RA+1/TG0)*Ps
RND=(1-Psym)/((1/A)*(1/GF-1)-B)-ag-RAD; print('RNDiff',RND)
