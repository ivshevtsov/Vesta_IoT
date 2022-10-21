import matplotlib.pyplot as plt
import skrf as rf

def z_input_impedance(network, in_port, f_range):
    f = network[f_range].f
    z11 = network[f_range].z[:, in_port - 1, in_port - 1]
    z12 = network[f_range].z[:, in_port - 1, in_port]
    z22 = network[f_range].z[:, in_port, in_port]
    z21 = network[f_range].z[:, in_port, in_port - 1]
    zin = z11 - (z21 * z12 / (z22 + 50))
    return f, zin

HOME = 'DATA/LNA_MAXIM/sNp'
lna_list = ['MAX2679', 'MAX2686', 'MAX2693L', 'MAX2659']


lna_wo_match = rf.Network(f'{HOME}/lna_wo_match.s8p')
lna_w_match = rf.Network(f'{HOME}/lna_w_match.s8p')

'''
lna_wo_match.plot_s_smith(0, 0, label=lna_list[0])
lna_wo_match.plot_s_smith(2, 2, label=lna_list[1])
lna_wo_match.plot_s_smith(4, 4, label=lna_list[2])
lna_wo_match.plot_s_smith(6, 6, label=lna_list[3])

plt.figure()
lna_wo_match.plot_s_db(0, 0, label=lna_list[0])
lna_wo_match.plot_s_db(2, 2, label=lna_list[1])
lna_wo_match.plot_s_db(4, 4, label=lna_list[2])
lna_wo_match.plot_s_db(6, 6, label=lna_list[3])


plt.figure()
lna_wo_match.plot_z_re(0, 0, label=lna_list[0])
lna_wo_match.plot_z_re(2, 2, label=lna_list[1])
lna_wo_match.plot_z_re(4, 4, label=lna_list[2])
lna_wo_match.plot_z_re(6, 6, label=lna_list[3])

plt.figure()
lna_wo_match.plot_z_im(0, 0, label=lna_list[0])
lna_wo_match.plot_z_im(2, 2, label=lna_list[1])
lna_wo_match.plot_z_im(4, 4, label=lna_list[2])
lna_wo_match.plot_z_im(6, 6, label=lna_list[3])
'''



freq = '1-3ghz'

#print(lna_wo_match[freq].s_mag[0,0,0])
#print(lna_wo_match[freq].s_deg[0 ,0,0])


#print(lna_wo_match[freq].s_re[0 ,0,0])
#print(lna_wo_match[freq].s_im[0,0,0])
f, Zin_0 = z_input_impedance(network=lna_wo_match, in_port=1, f_range='1-2ghz')
f, Zin_1 = z_input_impedance(network=lna_wo_match, in_port=3, f_range='1-2ghz')
f, Zin_2 = z_input_impedance(network=lna_wo_match, in_port=5, f_range='1-2ghz')
f, Zin_3 = z_input_impedance(network=lna_wo_match, in_port=7, f_range='1-2ghz')

plt.figure()
plt.plot(f, Zin_0.real, label = lna_list[0])
plt.plot(f, Zin_1.real, label = lna_list[1])
plt.plot(f, Zin_2.real, label = lna_list[2])
plt.plot(f, Zin_3.real, label = lna_list[3])
plt.legend()
plt.grid()

plt.figure()
plt.plot(f, Zin_0.imag, label = lna_list[0])
plt.plot(f, Zin_1.imag, label = lna_list[1])
plt.plot(f, Zin_2.imag, label = lna_list[2])
plt.plot(f, Zin_3.imag, label = lna_list[3])
plt.legend()
plt.grid()

plt.figure()
port = 7
lna_wo_match['1.6ghz'].plot_s_smith(port-1, port-1, label=lna_list[0]+'wo', marker='o')
lna_w_match['1.6ghz'].plot_s_smith(port-1, port-1, label=lna_list[0]+'w', marker='o')

plt.show()