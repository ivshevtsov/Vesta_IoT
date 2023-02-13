import numpy as np
import matplotlib.pyplot as plt
import control

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#Calculation MFB filter
#Initial Data
Q = 0.707
Gain_db = 0
Gain = 10**(Gain_db/20)
F_3db = 0.9e6

R1 = 60e3
R2 = R1/10
R3 = Gain*R1
C1 = Q*(R2*R3 + R1*R3 + R1*R2)/(2*np.pi*F_3db*R1*R2*R3)
C2 = 1/((2*np.pi*F_3db)**2 * C1*R2*R3)

print(f'C1={C1*1e12} пФ')
print(f'C1(diff)={C1*1e12*0.5} пФ')
print(f'C2={C2*1e12} пФ')
print(f'R1={R1} Ом')
print(f'R2={R2} Ом')
print(f'R3={R3} Ом')

Q_calc = (2*np.pi*F_3db*C1*R1*R2*R3)/(R2*R3 + R1*R3 + R1*R2)
F3db_calc = (1/(C1*C2*R2*R3)**(1/2))*(1/(2*np.pi))

s= control.tf('s')
Fmin = 0
Fmax =  50e6
omega = np.linspace( Fmin, Fmax, 1000)
TF = Gain*(F3db_calc**2) / ((s)**2 + (s)*(F3db_calc / Q_calc) + F3db_calc**2)
mag, ph, w = control.bode(TF, plot=False, color='Tab:red', Hz = True, omega=omega)
plt.figure()
plt.plot(w, 20*np.log10(mag), color='Tab:red', linewidth='3')
plt.grid(which='both', axis='both')
plt.show()