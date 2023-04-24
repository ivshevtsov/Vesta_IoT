import numpy as np

Vpp_in = 570e-6
Vpp_out = 2*1.7e-3

Gain = 20*np.log10(Vpp_out/Vpp_in)
print(Gain)

