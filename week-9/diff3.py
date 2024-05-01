import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
def returns_dydt(y,t):
	dydt=(1-y)/(1.95-y) - y/(0.05+y)
	return dydt
y0=[0,1,2]
t=np.linspace(1,10)
y=odeint(returns_dydt,y0,t)
plt.plot(t,y)
plt.plot("time")
plt.plot("y")
plt.show()
