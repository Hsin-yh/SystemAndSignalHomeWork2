import numpy as np
import matplotlib.pyplot as plt
def unit(t):
     r=np.where(t>0.0,1.0,0.0)
     return r
t=np.linspace(-1.0,3.0,1000)
plt.ylim(-1.0,3.0)
plt.plot(t,unit(t))
plt.show()