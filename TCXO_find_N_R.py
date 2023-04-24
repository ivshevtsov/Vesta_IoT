

TCXO = 19.2e6
F_out = 1588e6

maxR = 2**6
maxN = 2**11


for N in range(1,maxN):
    for R in range(1,maxR):
        F = TCXO*N/R
        if abs(F-F_out)<500e3:
            print(f'N={N}, R={R}')

print(f'Channel spacing {F_out/maxN} Hz')