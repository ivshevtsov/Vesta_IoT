import matplotlib.pyplot as plt
import numpy as np
import docx

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def write_table(directory, file, N_Table, n_rows, ):
    doc = docx.Document(f'{directory}/{file}')
    table = doc.tables[N_Table]
    for row in range(n_rows):
        Title = table.rows[row+1].cells[0].text
        min=    table.rows[row+1].cells[1].text
        typ=    table.rows[row+1].cells[2].text
        max=    table.rows[row+1].cells[3].text
        mism =  table.rows[row+1].cells[4].text

        if is_number(min) and is_number(typ) and is_number(max) and is_number(mism):
            min = float(min)
            typ = float(typ)
            max = float(max)
            mism = float(mism)

            min_glob = abs((typ-min)/3)
            max_glob = abs((typ-max)/3)
            min_total = typ - 3*(min_glob**2+mism**2)**0.5
            max_total = typ + 3*(max_glob**2+mism**2)**0.5
            string = f'{round(min_total, 2)}\n{round(max_total, 2)}'
            string_py = f'{round(min_total, 2)}<>{round(max_total, 2)}'
            table.rows[row+1].cells[5].text = string
            print(f'{Title} {min} {typ} {max} {mism} {string_py}')

    doc.save(f'{directory}/{file}')

File_H = 'H_CSCS_21_11_Ph_err_NF_G_err.csv'
File_L = 'L_CSCS_21_11_Ph_err_NF_G_err.csv'
Data_H = np.genfromtxt(f'DATA/LNA/{File_H}', delimiter=',', skip_header=1)
Data_L = np.genfromtxt(f'DATA/LNA/{File_L}', delimiter=',', skip_header=1)

#work with table
#write_table(directory='DATA/LNA', file='LNA_Results(24.06.22).docx', N_Table=1, n_rows=13)
#write_table(directory='DATA/LNA', file='LNA_Results(24.06.22).docx', N_Table=2, n_rows=13)


#Plot S21/S11
plt.figure()
plt.plot(Data_H[10:,0], Data_H[10:,1],label='Gain Max', linewidth=3)
plt.plot(Data_L[10:,0], Data_L[10:,1],label='Gain Low', linewidth=3)
plt.plot(Data_H[10:,0], Data_H[10:,2],label='S11', linewidth=3)
plt.xlabel('F, Гц')
plt.ylabel('дБ')
plt.legend()
plt.grid(which='both', axis='both')
plt.savefig(f'DATA/LNA/Gain_S11_Max')

#Plot NF
plt.figure()
plt.plot(Data_H[10:,0], Data_H[10:,4], label='NF(Gain Max)', linewidth=3)
plt.plot(Data_L[10:,0], Data_L[10:,4], label='NF(Gain Low)', linewidth=3)
plt.xlabel('F, Гц')
plt.ylabel('NF, дБ')
plt.legend()
plt.grid(which='both', axis='both')
plt.savefig(f'DATA/LNA/NF_Max')


#Plot Gain Error
plt.figure()
plt.plot(Data_H[10:,0], Data_H[10:,5], label='Gain Max', linewidth=3)
plt.plot(Data_L[10:,0], Data_L[10:,5], label='Gain Low', linewidth=3)
plt.xlabel('F, Гц')
plt.ylabel('Gain Error, дБ')
plt.legend()
plt.grid(which='both', axis='both')
plt.savefig(f'DATA/LNA/Gain_error')

#Plot Phase Error
plt.figure()
plt.plot(Data_H[10:,0], Data_H[10:,3], label='Gain Max', linewidth=3)
plt.plot(Data_L[10:,0], Data_L[10:,3], label='Gain Low', linewidth=3)
plt.xlabel('F, Гц')
plt.ylabel('Phase Error, град.')
plt.legend()
plt.grid(which='both', axis='both')
plt.savefig(f'DATA/LNA/Phase_error')


#Errors
fig, ax1 = plt.subplots()
color = 'tab:orange'
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Gain Error, дБ', color=color)
ax1.plot(Data_H[10:,0], Data_H[10:,5], color=color, linewidth=3)
ax1.tick_params(axis='y', labelcolor=color)
plt.grid(which='both', axis='both')
# Adding Twin Axes to plot using dataset_2
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Phase Error, град.', color=color)
ax2.plot(Data_H[10:,0], Data_H[10:,3], color=color, linewidth=3)
ax2.tick_params(axis='y', labelcolor=color)
plt.savefig(f'DATA/LNA/Errors_Max')

plt.show()