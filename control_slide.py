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
t1_new=[]
tspan=np.linspace(0,20,500)
a=np.linspace(1,10,20)
q=[[1,0],[2,0],[6,0]]
t_last=0
for y0 in q:
    if(y0[0]+y0[1]<0):
        for j in range(30):
            ys1=sc.odeint(f1,y0,tspan)
            for cnt in range(len(ys1)):
                if(m*ys1[cnt,0]+ys1[cnt,1]<0):
                    amar10.append(ys1[cnt,0])
                    amar11.append(ys1[cnt,1])
                    ctr1.append(1)
                    t1.append(tspan[cnt])
                    t1_new=[t_last+i for i in t1]

                elif(m*ys1[cnt,0]+ys1[cnt,1]>0):
                    var0=ys1[cnt,0].copy()
                    var1=ys1[cnt,1].copy()
                    c1.append(len(t1))

                    break
            print(len(t1_new))
            print(len(ctr1))
 
            t_last=t1_new[len(t1_new)-1]
            plt.plot(amar10,amar11,'go')
            if len(c1)==1:
                plt.figure(2)
                plt.plot(t1_new,ctr1)
            else:
                plt.figure(2)
                plt.plot(t1_new[c1[len(c1)-2]:c1[len(c1)-1]],ctr1)
            ys2=sc.odeint(f2,[var0,var1],tspan)
            for i in range(len(ys2)):
                if(m*ys2[i,0]+ys2[i,1]>0):
                    amar20.append(ys2[i,0])
                    amar21.append(ys2[i,1])
                    ctr2.append(-1)
                    t1.append(tspan[i]) 

                elif(m*ys2[i,0]+ys2[i,1]<0):
                    y01=ys2[i,0].copy()
                    y02=ys2[i,1].copy()
                    y0=[y01,y02]
                    c1.append(len(t1))
                    break
            t1_new=[t_last+i for i in t1]
            t_last=t1_new[len(t1_new)-1]
            plt.figure(1)
            plt.plot(amar20,amar21,'ro')        
            plt.figure(2)
            plt.plot(t1_new[c1[len(c1)-2]:c1[len(c1)-1]],ctr2)
        x=np.linspace(-3,3,100)
        e=-x
        plt.figure(1)
        plt.plot(x,e,'r--')
        plt.grid()
        #plt.savefig('sarah_spurgeon2.eps')
        plt.show()
        
    
    
    elif(y0[0]+y0[1]>0):
        for j in range(30):
            ys2=sc.odeint(f2,y0,tspan)
            for cnt in range(len(ys2)):
                if(m*ys2[cnt,0]+ys2[cnt,1]>0):
                    amar20.append(ys2[cnt,0])
                    amar21.append(ys2[cnt,1])
                    t1.append(tspan[cnt])

                elif(m*ys2[cnt,0]+ys2[cnt,1]<0):
                    var0=ys2[cnt,0].copy()
                    var1=ys2[cnt,1].copy()
                    c1.append(len(t1))
                    print(len(t1))
                    break
            
            plt.plot(amar20,amar21,'go')
            if len(c1)==1:
                plt.figure(2)
                t1_new=[t_last+i for i in t1]
                ctr1=[-1]*len(t1_new)
                plt.plot(t1_new,ctr1)
                print(t1_new)
                t_last=t1_new[len(t1_new)-1]

            else:
                t1_new=[t_last+i for i in t1[c1[len(c1)-2]:]]
                print t1_new[c1[len(c1)-2]:]
                ctr1=[-1]*len(t1_new) 
                plt.figure(2) 
                plt.plot(t1_new[c1[len(c1)-2]:],ctr1)
                t_last=t1_new[len(t1_new)-1]
            ys1=sc.odeint(f1,[var0,var1],tspan)
            for i in range(len(ys1)):
                if(m*ys1[i,0]+ys1[i,1]<0):
                    amar10.append(ys1[i,0])
                    amar11.append(ys1[i,1])
                    t1.append(tspan[i])

                elif(m*ys1[i,0]+ys1[i,1]>0):
                    y01=ys1[i,0].copy()
                    y02=ys1[i,1].copy()
                    y0=[y01,y02]
                    c1.append(len(t1))
                    break
            print(t1)
            print(len(t1))
            print(c1[len(c1)-2])
            print t_last
            t1_new=[t_last+i for i in t1[c1[len(c1)-2]:]]
            t_last=t1[len(t1_new)-1]
            print(len(t1_new[c1[len(c1)-2]:]))
            plt.figure(1)
            plt.plot(amar10,amar11,'ro')         
            ctr2=[1]*len(t1_new)
            plt.figure(2)
            plt.plot(t1_new[c1[len(c1)-2]:],ctr2)
        x=np.linspace(-3,3,100)
        e=-x
        plt.figure(1)
        plt.plot(x,e,'r--')
        plt.grid()
        #plt.savefig('sarah_spurgeon2.eps')
        plt.show()

