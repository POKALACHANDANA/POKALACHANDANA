import csv
import numpy as np
t=np.arange(0,1,0.01)
f=6
x=np.sin(2*np.pi*f*t)
with open("cs.csv","wb") as k:
	k.write(x)r.g
