
unCox = 150e-6
upCox = 55e-6
Lmin = 1e-6

gm = 180e-6

Veff = 0.15

Id = gm*Veff/2
Iss = Id*2


Wn_in = 2*Id*Lmin/(unCox*Veff**2)
Wp_load = 2*Id*Lmin/(upCox*Veff**2)


print(Wn_in)
print(Wp_load)
print(Id)
print(Iss)