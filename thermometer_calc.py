import numpy as np

Vin_min = 0.4
Vin_max = 0.8

Vref = 1.2

Vcm = 0.9

Vin_negative = np.linspace(Vin_min-Vcm, Vin_max-Vcm, 100)
Vref_positive = Vref-Vcm
#print(Vin_negative)
#print(Vref_positive)

T1 = 1e-3
T2 = 2e-3
R  = 400e6
C  = 2.5e-12

V1 = Vin_negative[0]*T1/(R*C)
V2 = Vref_positive*T2/(R*C)
print(f'Voltage 1 {V1}')
print(f'Voltage 1 {V2}')
print(f'Freq clk {2**10/T2*1e-6} MHz')



