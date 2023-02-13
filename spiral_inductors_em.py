import matplotlib.pyplot as plt
import numpy as np
import skrf as rf
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


def z_input_impedance(network, in_port, f_range):
    f = network[f_range].f
    z11 = network[f_range].z[:, in_port - 1, in_port - 1]
    z12 = network[f_range].z[:, in_port - 1, in_port]
    z22 = network[f_range].z[:, in_port, in_port]
    z21 = network[f_range].z[:, in_port, in_port - 1]
    zin = z11 - (z21 * z12 / (z22 + 50))
    return f, zin

HOME = 'DATA/Y_inductor'

File_EM1 = f'{HOME}/EM1_sim.s1p'
File_EM2 = f'{HOME}/EM2_sim.s1p'
File_TSMC = f'{HOME}/TSMC_sim.s1p'
EM1_sim = rf.Network(File_EM1)
EM2_sim = rf.Network(File_EM2)
TSMC_sim = rf.Network(File_TSMC)