import matplotlib.pyplot as plt
import numpy as np

Rin=5e3
Gain_db=20
Gain=10**(Gain_db/20)
N=5

Rf=(Rin*Gain-Rin)/(2**N)
print(Rf)



Gain_Error=[]
G=[]
for i in range(2**N+1):
    print(Rin+i*Rf)
    G.append(20 * np.log10((Rin+i*Rf)/Rin))

print(G, sep='\n')

for i in range(len(G)-1):
    Gain_Error.append(abs(G[i]-G[i+1]))


plt.figure()
plt.plot(G, 'o')
plt.grid()

plt.figure()
plt.plot(Gain_Error, 'o')
plt.grid()
plt.show()
