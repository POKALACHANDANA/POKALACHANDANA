import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
f1=4
f2=2
x=np.sin(2*np.pi*f1*t)
y=np.sin(2*np.pi*f2*t)
z=x-y
plt.plot(t,z)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('sine wave')
plt.show()
