import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import scipy.stats as st

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


def plot_csv_column(data, column_x, column_y, xlabel, ylabel, label, percent):
    len_data = int(len(data[:, column_x-1])*percent/100)
    plt.plot(data[:len_data, column_x-1], data[:len_data, column_y-1], label=label, linewidth='2')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()




HOME = 'DATA/VGA_MODEM_PEX/csv'

File_reg_G1 = 'vga_modem_reg_G1_p1db_sch.csv'
File_reg_G2 = 'vga_modem_reg_G2_p1db_sch.csv'
File_reg_G3 = 'vga_modem_reg_G3_p1db_sch.csv'

REG_1 = genfromtxt(f'{HOME}/{File_reg_G1}', delimiter=',', skip_header=1)
REG_2 = genfromtxt(f'{HOME}/{File_reg_G2}', delimiter=',', skip_header=1)
REG_3 = genfromtxt(f'{HOME}/{File_reg_G3}', delimiter=',', skip_header=1)

# plot reg gain
plt.figure()
plot_csv_column(REG_1, column_x=1, column_y=2, xlabel='N', ylabel='P1dB(IN), дБм', percent=100, label='G1(G2=0, G3=0)')
plot_csv_column(REG_2, column_x=1, column_y=2, xlabel='N', ylabel='P1dB(IN), дБм', percent=100, label='G2(G1=14,G3=0)')
plot_csv_column(REG_3, column_x=1, column_y=2, xlabel='N', ylabel='P1dB(IN), дБм', percent=100, label='G3(G1=14,G2=14)')
plt.grid()








plt.show()