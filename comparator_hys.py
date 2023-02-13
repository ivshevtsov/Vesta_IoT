from scipy.optimize import fsolve

#Solve equation with resistors
def divider(p):
    V4 = 0.4
    V3 = 0.8
    V2 = 2.4
    V1 = 2.8
    Id = 25e-6
    VDD = 3.3
    R1,R2,R3,R4,R5=p
    return (VDD/(R1+R2+R3+R4+R5)-Id,
            VDD/(R1+R2+R3+R4+R5)*(R2+R3+R4+R5)-V1,
            VDD/(R1+R2+R3+R4+R5)*(R3+R4+R5)-V2,
            VDD/(R1+R2+R3+R4+R5)*(R4+R5)-V3,
            VDD/(R1+R2+R3+R4+R5)*(R5)-V4)
R1,R2,R3,R4,R5 = fsolve(divider, (1,1,1,1,1))
print('Find resistance for divider')
print(f'R1 = {R1/1000} kOhm')
print(f'R2 = {R2/1000} kOhm')
print(f'R3 = {R3/1000} kOhm')
print(f'R4 = {R4/1000} kOhm')
print(f'R5 = {R5/1000} kOhm')
print('Calculation error')
print(divider((R1,R2,R3,R4,R5)))
print('###########################')
##-------------------##


Vth = 0.65
unCox = 155e-6
upCox = 55e-6
Ibias = 15e-6
L = 2e-6
Veff = 0.18
a = 2

#P - comparator

Wp_in = 2*Ibias*0.5*L/(upCox*Veff**2)
Wn_load = 2*Ibias*0.5*L/(unCox*Veff**2)
Wn_hys = a*Wn_load
i1=Ibias/(1+a)
i2=Ibias-i1
Vgs1 = (2*i1/((Wp_in/L)*upCox))**0.5 + Vth
Vgs2=  (2*i2/((Wp_in/L)*upCox))**0.5 + Vth
V_hys_p = Vgs2 - Vgs1

print(f'Width p input {Wp_in}')
print(f'Mirroring {a}')
print(f'Hysteresis voltage {V_hys_p}')
print(f'Width n load {Wn_load}')
print(f'Width n hys {Wn_hys}')
print(f'Common channel length {L}')
print('###########################')

#N - comparator
Wn_in = 2*Ibias*0.5*L/(unCox*Veff**2)
Wp_load = 2*Ibias*0.5*L/(upCox*Veff**2)
Wp_hys = a*Wp_load
i1=Ibias/(1+a)
i2=Ibias-i1
Vgs1 = (2*i1/((Wn_in/L)*unCox))**0.5 + Vth
Vgs2=  (2*i2/((Wn_in/L)*unCox))**0.5 + Vth
V_hys_n = Vgs2 - Vgs1

print(f'Width n input {Wn_in}')
print(f'Mirroring {a}')
print(f'Hysteresis voltage {V_hys_n}')
print(f'Width p load {Wp_load}')
print(f'Width p hys {Wp_hys}')
print(f'Common channel length {L}')
print('###########################')
print(f'YOU CAN CHANGE LENGTH!!')

V = 1.789
I = 15e-6
print(f'Bias resistance {V/I}')