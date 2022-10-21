#Constants for Transistors
import numpy as np

K=7.037e-25
hamma = 0.691

T=300
k=1.38e-23

upCox=55e-6
unCox=150e-6
Cox=4.29e-3

L_test=550e-9

lambda_p=40e-3
lambda_n=80e-3


##initial requirements

G_db=20
f = 3e6
CL = 1e-12
PM=70
Veff=0.2
L=1e-6

##convert db to mag
G=10**(G_db/20)

##calculation
GBP=G*f*2*np.pi

w2=4*GBP
w0=8*GBP

CF = (w2/w0)*CL

gm1 = GBP*CF
gm2 = 8*gm1

I_M1 = Veff*gm1/2
I_Tail=I_M1*2
I_Out = Veff*gm2/2
I_Total = I_Tail+I_Out*2


Wp_IN = 2*I_M1*L/(upCox*Veff**2)
Wp_TAIL = 2*(I_M1*2)*L/(upCox*Veff**2)
Wn_LOAD = 2*I_M1*L/(unCox*Veff**2)
Wn_OUT = 2*I_Out*L/(unCox*Veff**2)

print(f'gm1={gm1*1e6} uS')
print(f'gm1={gm2*1e6} uS')

print(f'M1 current={I_M1*1e6} uA')
print(f'Out current={I_Out*1e6} uA')

print(f'Input transistor width={Wp_IN*1e6} um')
print(f'Tail transistor width={Wp_TAIL*1e6} um')
print(f'Load transistor width={Wn_LOAD*1e6} um')
print(f'Out transistor width={Wn_OUT*1e6} um')
print(CF)
print(1/gm2)