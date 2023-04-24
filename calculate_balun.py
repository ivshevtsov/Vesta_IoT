unCox = 155e-6
Vth = 0.6
Veff = 0.25
L = 0.55e-6

RL = 150

gm = 1/RL

Id = gm*Veff/2

print(f'Curren {Id*1e3} mA')
print(f'drop voltage {Id*RL}')
print(f'Gm {gm*1e3} mS')
W = 2*Id*L/(unCox*Veff**2)

print(f'Width of transistor {W*1e6} um')


