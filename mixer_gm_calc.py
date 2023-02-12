import numpy as np

gm=5e-3
RL=1.5e3
unCox = 155e-6
upCox = 50e-6
L = 0.55e-6

Gain  = 20*np.log10(gm*RL*(2**0.5)/(np.pi))

print(Gain)
Veff = 0.57
Id = gm*0.5*Veff/2

Wn = gm*0.5*L/(unCox*Veff)
Wp = gm*0.5*L/(upCox*Veff)

print(Id*1e6)
print(Wn*1e6)
print(Wp*1e6)

print(1/(Wn*Veff))