import numpy as np
GPS = 1

if GPS==1:
    F_LPF=2.5e6
    F_PPF = 13.3e6
    R=20e3
elif GPS==0:
    F_LPF = 5e6
    F_PPF = 13.3e6
    R = 5e3
else:
    F_LPF = 20e6
    F_PPF = 1e-6
    R = 5e3

#---Inition Conditions---
C = 1/(2*np.pi*F_LPF*R)
Overlap_C = 70
N_Bit = 5

Min_Cap = C*(1-Overlap_C/100)
Max_Cap = C*(1+Overlap_C/100)
Unity_Cap = (Max_Cap-Min_Cap)/2**N_Bit
List_Cap = [Min_Cap]
for i in range(N_Bit):
    Cap = Unity_Cap*(2**i)
    List_Cap.append(Cap)
#------------------------


print(f'Максимальная емкость: {Max_Cap} Ф')
print(f'Минимальная  емкость: {Min_Cap} Ф')
print(f'Типовая емкость: {C}')
print('Элементы банка конденсаторов')
print(*List_Cap, sep="\n")

print('##--------------##')
R_PPF = 1/(2*np.pi*C*F_PPF)
print(f'Сопротивление R_PPF:{round(R_PPF, 2)} Ом')

print('##--------------##')
print(f'Тактовая частота:{round(F_LPF*2*np.pi/1e6, 2)} МГц')

print(R/R_PPF)