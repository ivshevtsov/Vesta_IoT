import numpy as np


F_low = 2e6
C = 1e-12


R = 1/(2*np.pi*C*F_low)

print(f'R={R*1e-3} kOhm, C={C*1e12} pF')
