
N_max = 2**11
R_max = 2**6
TCXO = 19.2e6
Fout = 1571e6

error_F = 250e3

for N in range(1,N_max):
    for R in range(1, R_max):
        F = TCXO*N/R
        deltaF = abs(F-Fout)
        if deltaF<error_F:
            print(f'N ={N}, R={R}, deltaFF={round(deltaF*1e-3,2)} kHz')

print(f'Frequency step = {Fout/N_max*1e-3} kHz')