import scipy.integrate as sc
import numpy as np
import sympy as sm
import matplotlib.pyplot as plt

m=1
def f1(Y,t):
    x,y=Y
    return[y,1]

def f2(Y,t):
    x,y=Y
    return[y,-1]

def f3(Y,t):
    x,y=Y
    return[y,0]

amar10=[]
amar11=[]
amar20=[]
amar21=[]
ctr1=[]
ctr2=[]
t1=[]
t2=[]
cnt=0
i=0
c1=[]
c2=[]
tspan=np.linspace(0,20,500)
a=np.linspace(1,10,20)
q=[[1,0],[2,0],[6,0]]
for y0 in q:
    for j in range(30):
        ys1=sc.odeint(f1,y0,tspan)
        for cnt in range(len(ys1)):
            if(m*ys1[cnt,0]+ys1[cnt,1]<0):
                amar10.append(ys1[cnt,0])
                amar11.append(ys1[cnt,1])
                ctr1.append(1)
                t1.append(tspan[cnt])
                
            elif(m*ys1[cnt,0]+ys1[cnt,1]>0):
                var0=ys1[cnt,0].copy()
                var1=ys1[cnt,1].copy()
                c1.append(cnt)
                break
        print(t1)
        plt.plot(amar10,amar11,'go')    
        ys2=sc.odeint(f2,[var0,var1],tspan)
        for i in range(len(ys2)):
            if(m*ys2[i,0]+ys2[i,1]>0):
                amar20.append(ys2[i,0])
                amar21.append(ys2[i,1])
                ctr2.append(-1)
                t2.append(tspan[cnt])

            elif(m*ys2[i,0]+ys2[i,1]<0):
                y01=ys2[i,0].copy()
                y02=ys2[i,1].copy()
                y0=[y01,y02]
                break
        plt.plot(amar20,amar21,'ro')        
        #print y0
    
x=np.linspace(-3,3,100)
e=-x
plt.plot(x,e,'r--')
plt.grid()
plt.show()
plt.figure(2)
plt.plot(t1,ctr1)
#plt.plot(tspan,ys2)
plt.grid()
#plt.savefig('sarah_spurgeon2.eps')
plt.show()

