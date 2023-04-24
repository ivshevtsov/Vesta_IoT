import math
V_min = 0.5
V_max = 0.7
V_ref = 1.1
ID_T = 50e-6
BITS = 8

R3 = V_min/ID_T
R2 = (V_max - ID_T*R3)/ID_T
R1 = (V_ref-ID_T*R3 - ID_T*R2)/ID_T

delta_R2 = R2/BITS
delta_Vr = ID_T*delta_R2
delta_Te = delta_Vr/1.81e-3

R1 = round(R1)
R2 = round(R2)
R3 = round(R3)
delta_R2 = round(delta_R2)

print(f'R1 {R1}')
print(f'R2 {R2}')
print(f'R3 {R3}')

print(f'delta R2 {delta_R2} Ohm')
print(f'delta Vr {delta_Vr} V')
print(f'delta Te (LSB) {delta_Te} C')


R_Cell = math.gcd(math.gcd(R1, R3), math.gcd(R2, delta_R2))

print(f'R Cell {R_Cell} Ohm')