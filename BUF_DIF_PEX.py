import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import scipy.stats as st

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


def plot_csv_column(data, column_x, column_y, xlabel, ylabel, percent):
    len_data = int(len(data[:, column_x-1])*percent/100)
    plt.plot(data[:len_data, column_x-1], data[:len_data, column_y-1], linewidth='2')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)



HOME = 'DATA/BUF_DIF_PEX/csv'
File_PVT = 'buf_dif_pvt_pex_plot.csv'

PVT = genfromtxt(f'{HOME}/{File_PVT}', delimiter=',', skip_header=1)

# plot S21
plt.figure()
plot_csv_column(PVT, column_x=5, column_y=6, xlabel='f, Гц', ylabel='S21, дБ', percent=100)
plt.xscale('log')
plt.grid()

# plot S22
plt.figure()
plot_csv_column(PVT, column_x=3, column_y=4, xlabel='f, Гц', ylabel='S22,S11, дБ', percent=100)
plt.xscale('log')
plt.grid()

# plot NF
plt.figure()
plot_csv_column(PVT, column_x=1, column_y=2, xlabel='f, Гц', ylabel='NF, дБ', percent=100)
plt.xscale('log')
plt.grid()

plt.show()