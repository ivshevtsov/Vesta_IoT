import numpy as np

f1 = 3e6

R1 = 50e3

C = 1/(2*np.pi*R1*f1)

print(f'Cap={C*1e12} pF')