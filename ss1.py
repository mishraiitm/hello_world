import scipy.integrate as sc
import numpy as np
import sympy as sm
import matplotlib.pyplot as plt
sgn = lambda x,eps:(x<-eps)*(-1)+(x>=-eps and x<eps)*0+(x>=eps)*1

def f1(Y,t):
    x,y=Y
    f=x+y
    return[y,-sgn(f,1e-7)]
<<<<<<< HEAD

t_end=500
t_start=1
t_step=1
t_interval=np.arange(t_start,t_end,t_step)

=======
amar10=[]
amar11=[]
amar20=[]
amar21=[]
cnt=0
i=0
tspan=np.linspace(1,20,500)
>>>>>>> e8059feaf3bc7e127e4ae962910e12180019f108
y0=[-0.5,0.5]
ts=[]
ys=[]
ode=sc.ode(f1)
ode.set_integrator('vode',nsteps=500,method='bdf')    
<<<<<<< HEAD
ode.set_initial_value(y0,t_start)
while ode.successful() and ode.t < t_end:
    ode.integrate(ode.t + t_step)
=======
ode.set_interval_alue(Y,tspan[0])
while ode.successful() and ode.t < tspan[-1]:
    ode.integrate(ode.t + ode.(tspan[1]-tspan[0])
>>>>>>> e8059feaf3bc7e127e4ae962910e12180019f108
    ts.append(ode.t)
    ys.append(ode.y)

t=np.vstack(ts)
s,i,r=np.vstack(ys).T
plt.plot(t,s)
plt.grid()
#plt.savefig('stateswitch1.eps')
plt.show()


