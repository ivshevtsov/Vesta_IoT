import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import scipy.stats as st

#plt.rcParams["font.family"] = "Century Gothic"
#plt.rcParams["font.size"] = "14"


def plot_csv_column(data, column_x, column_y, xlabel, ylabel, percent):
    len_data = int(len(data[:, column_x-1])*percent/100)
    plt.plot(data[:len_data, column_x-1], data[:len_data, column_y-1], linewidth='2')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def plot_csv_hist_column(data, column):

    plt.hist(data[:, column-1], density=True,  facecolor='g')
    mn, mx = plt.xlim()
    plt.xlim(mn, mx)
    kde_xs = np.linspace(mn, mx, 300)
    kde = st.gaussian_kde(data[:, column-1])
    plt.plot(kde_xs, kde.pdf(kde_xs), label="PDF")
    mu = np.mean(data[:, column-1])
    std = np.std(data[:, column-1])
    plt.title(fr'$\mu$={round(mu/1e6, 2)}МГц, $\sigma$={round(std/1e3, 2)}кГц')
    plt.ylabel('Probability')

    plt.figure()
    print(len(data[:, column - 1]))
    for i in range(len(data[:, column-1])):
        #require give list for histogramm
        plt.plot(i, np.std(data[:i+1, column-1]),'o', linewidth='2')


HOME = 'DATA/PPF/csv'
File_PVT = 'gps_pvt_sch.csv'
File_TOTAL = 'glo_total_sch.csv'
PVT = genfromtxt(f'{HOME}/{File_PVT}', delimiter=',', skip_header=1)
TOTAL = genfromtxt(f'{HOME}/{File_TOTAL}', delimiter=',', skip_header=1)

# plot HF
plt.figure()
plot_csv_column(PVT, column_x=1, column_y=2, xlabel='f, Гц', ylabel='HF, дБ', percent=60)
plt.grid()

# plot GD
plt.figure()
plot_csv_column(PVT, column_x=3, column_y=4, xlabel='f, Гц', ylabel='GD, с', percent=60)
plt.grid()

# plot NF
plt.figure()
plot_csv_column(PVT, column_x=5, column_y=6, xlabel='f, Гц', ylabel='NF, дБ', percent=100)
plt.grid()

plt.figure()
plot_csv_hist_column(TOTAL, column=1)
plt.grid()

plt.show()
