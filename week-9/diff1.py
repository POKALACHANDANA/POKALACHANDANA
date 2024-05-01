import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def return_dydt (y,t):
	dydt=-y*t+13
	return dydt
y0=1
t=np.linspace(0,5)
y=odeint(return_dydt,y0,t)
plt.plot(t,y)
plt.xlabel("time")
plt.ylabel("y")
plt.show()
