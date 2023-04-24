import numpy as np

fc = 950e6
Cpad = 1.2e-12
Ls = 6e-9
Lg = 10e-9
Veff = 0.2
Rs = 50
L = 0.55e-6
unCox = 155e-6


Cgs = 1/((Ls + Lg)*(2*np.pi*fc)**2) - Cpad
Cap_coeff = (Cgs/(Cgs+Cpad))**2
wt = Rs/(Ls*Cap_coeff)

gm = wt*Cgs

Id = gm*Veff/2
Wn =  2*Id*L/(unCox*Veff**2)

RL = 10/gm

print(f'Cgs {Cgs*1e12} pF')
print(f'wt {wt/(2*np.pi)*1e-9} GHz')
print(f'gm {gm*1e3} mS')
print(f'Current {Id*1e3} mA')
print(f'Width mos {Wn*1e6} um')
print(f'Load resistance {RL} Ohm')

