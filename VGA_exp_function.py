import matplotlib.pyplot as plt
import numpy as np

min = 0.8
max = 2.5

x = np.linspace(min, max, 100)
y = np.linspace(min, max, 100)


VDD=3.3
Vth=0.6
a=1/(VDD-Vth)
k=0.1
num = (k+(1+a*x)**2)**0.5
den = (k+(1-a*x)**2)**0.5
Av = 20*np.log10(num/den)


plt.plot(x,y)
plt.plot(x,Av*2)

plt.grid()
plt.show()