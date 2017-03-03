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
            ys2=sc.odeint(f2,y0,tspan)
            for cnt in range(len(ys2)):
                if(m*ys2[cnt,0]+ys2[cnt,1]<0):
                    amar20.append(ys2[cnt,0])
                    amar21.append(ys2[cnt,1])
                    t1.append(tspan[cnt])

                elif(m*ys2[cnt,0]+ys2[cnt,1]>0):
                    var0=ys2[cnt,0].copy()
                    var1=ys2[cnt,1].copy()
                    c1.append(len(t1))
                    print(len(t1))
                    break
            
            plt.figure(0)
            plt.plot(amar20,amar21,'go')
            if len(c1)==1:
                plt.figure(2)
                p=[t_last+i for i in t1]
                for i in range(len(p)):
                    t1_new.append(p[i])
                '''Adding the last time instance from previous integration to this one.t_last holds the value of last time instance from previous integration.This step is necessary because the integration of system in this cycle will begin from 0'''
                ctr1=[1]*len(t1_new)
                plt.figure(1)
                plt.plot(t1_new,ctr1)
                #plt.show()
                print(t1_new)
                t_last=t1_new[len(t1_new)-1]

            else:
                p=[t_last+i for i in t1[c1[len(c1)-2]:]]
                for i in range(len(p)):
                    t1_new.append(p[i])

                print t1_new[c1[len(c1)-2]:]
                ctr1=[1]*len(t1_new[c1[len(c1)-2]:]) 
                plt.figure(1) 
                plt.plot(t1_new[c1[len(c1)-2]:],ctr1,'g-')
                t_last=t1_new[len(t1_new)-1]
            ys1=sc.odeint(f1,[var0,var1],tspan)
            for i in range(len(ys1)):
                if(m*ys1[i,0]+ys1[i,1]>0):
                    amar10.append(ys1[i,0])
                    amar11.append(ys1[i,1])
                    t1.append(tspan[i]) #Building time list

                elif(m*ys1[i,0]+ys1[i,1]<0):
                    y01=ys1[i,0].copy() 
                    '''initial points for next system'''
                    y02=ys1[i,1].copy()
                    y0=[y01,y02]
                    c1.append(len(t1)) 
                    '''Building a list of lengths of time,it will contain the length of tspan for which one system was integrated'''
                    break
            print(t1)
            print(len(t1))
            print(c1[len(c1)-2])
            print t_last
            print(t1[c1[len(c1)-2]:])
            p=[i+t_last for i in t1[c1[len(c1)-2]:]]
            for i in range(len(p)):
                t1_new.append(p[i])
            '''here i am adding t_last from previous integration to time instance from this integration only.However t1 contains time instances of previous integration as well,so to overcome that barrier I have used c1[len(c1)-2]-- it will give me the time instances for this integration cycle only'''
            t_last=t1_new[len(t1_new)-1]
            print(len(t1_new[c1[len(c1)-2]:]))
            print(t1_new)
            print(len(t1_new))
            
            plt.figure(0)
            plt.plot(amar10,amar11,'ro')         
            ctr2=[-1]*len(t1_new[c1[len(c1)-2]:])
            
            plt.figure(1)
            plt.plot(t1_new[c1[len(c1)-2]:],ctr2)
        x=np.linspace(-3,3,100)
        e=-x
        plt.figure(0)
        plt.plot(x,e,'r--')
        plt.grid()
        #plt.savefig('sarah_spurgeon2.eps')

        
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
            
            plt.figure(0)
            plt.plot(amar20,amar21,'go')
            if len(c1)==1:
                plt.figure(2)
                p=[t_last+i for i in t1]
                for i in range(len(p)):
                    t1_new.append(p[i])
                '''Adding the last time instance from previous integration to this one.t_last holds the value of last time instance from previous integration.This step is necessary because the integration of system in this cycle will begin from 0'''
                ctr1=[-1]*len(t1_new)
                plt.figure(1)
                plt.plot(t1_new,ctr1)
                #plt.show()
                print(t1_new)
                t_last=t1_new[len(t1_new)-1]

            else:
                p=[t_last+i for i in t1[c1[len(c1)-2]:]]
                for i in range(len(p)):
                    t1_new.append(p[i])

                print t1_new[c1[len(c1)-2]:]
                ctr1=[-1]*len(t1_new[c1[len(c1)-2]:]) 
                plt.figure(1) 
                plt.plot(t1_new[c1[len(c1)-2]:],ctr1,'g-')
                t_last=t1_new[len(t1_new)-1]
            ys1=sc.odeint(f1,[var0,var1],tspan)
            for i in range(len(ys1)):
                if(m*ys1[i,0]+ys1[i,1]<0):
                    amar10.append(ys1[i,0])
                    amar11.append(ys1[i,1])
                    t1.append(tspan[i]) #Building time list

                elif(m*ys1[i,0]+ys1[i,1]>0):
                    y01=ys1[i,0].copy() 
                    '''initial points for next system'''
                    y02=ys1[i,1].copy()
                    y0=[y01,y02]
                    c1.append(len(t1)) 
                    '''Building a list of lengths of time,it will contain the length of tspan for which one system was integrated'''
                    break
            print(t1)
            print(len(t1))
            print(c1[len(c1)-2])
            print t_last
            print(t1[c1[len(c1)-2]:])
            p=[i+t_last for i in t1[c1[len(c1)-2]:]]
            for i in range(len(p)):
                t1_new.append(p[i])
            '''here i am adding t_last from previous integration to time instance from this integration only.However t1 contains time instances of previous integration as well,so to overcome that barrier I have used c1[len(c1)-2]-- it will give me the time instances for this integration cycle only'''
            t_last=t1_new[len(t1_new)-1]
            print(len(t1_new[c1[len(c1)-2]:]))
            print(t1_new)
            print(len(t1_new))
            
            plt.figure(0)
            plt.plot(amar10,amar11,'ro')         
            ctr2=[1]*len(t1_new[c1[len(c1)-2]:])
            
            plt.figure(1)
            plt.plot(t1_new[c1[len(c1)-2]:],ctr2)
        x=np.linspace(-3,3,100)
        e=-x
        plt.figure(0)
        plt.plot(x,e,'r--')
        plt.grid()
        #plt.savefig('sarah_spurgeon2.eps')
plt.show()

