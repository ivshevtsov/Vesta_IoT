
Diameter = 98.9
Pitch = 180
Chip_Size = 10000

Shrink = 0.9



# calculate characteristics
N_bumps = (Chip_Size-Diameter)/(Pitch)+1

print(f'Available number of bamps {int(N_bumps)}')
print(f'Diameter after shrink {Diameter*Shrink} um')
print(f'Pitch after shrink {Pitch*Shrink} um')
print(f'Chip size after shrink {Chip_Size*Shrink/1000} mm')

N_bumps = 55

X_First = (-Pitch*(N_bumps-1)/2)
Y_First = (Pitch*(N_bumps-1)/2)


XV = X_First
YV = Y_First
for y in range(55):
    for x in range(55):
        XV = X_First + (x) * Pitch
        YV = Y_First - (y) * Pitch
        print(XV, YV)


