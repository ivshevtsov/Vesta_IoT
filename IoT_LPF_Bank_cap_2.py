import numpy as np


F_LPF=0.5e6
R=25e3


#---Inition Conditions---
C = 1/(2*np.pi*F_LPF*R)
Overlap_C = 80
N_Bit = 4

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
print(f'Тактовая частота:{round(F_LPF*2*np.pi/1e6, 2)} МГц')
