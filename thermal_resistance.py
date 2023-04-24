Width_DIE = 10e-3
Length_DIE=10e-3
T_Ambient = 85
Power = 5

#Area DIE
Area_DIE = Width_DIE*Length_DIE

## DIE
h_DIE_Si = 700e-6
lamb_DIE_Si = 149

##compound
h_TIM = 100e-6
lamb_TIM = 1


High = [h_DIE_Si,    h_TIM]
lamb = [lamb_DIE_Si, lamb_TIM]
Title = ['DIE', 'Compound']


R_T=0
for i in range(len(High)):
    R_T_block = High[i]/(lamb[i]*Area_DIE)
    R_T_block = round(R_T_block, 3)
    R_T = R_T + R_T_block
    print('*-----------*')
    print(f'Тепловое сопротивление {Title[i]} = {R_T_block}')
    print(f'Изменение температуры {Title[i]} = {R_T_block*Power}')

T_chip = T_Ambient + R_T*Power
print('#----Results----#')
print(f'Тепловое сопротивление системы = {R_T}')
print(f'Температура окружающей среды =  {T_Ambient}')
print(f'Температура кристалла =  {T_chip}')
print(f'Изменение температуры =  {T_chip - T_Ambient}')
