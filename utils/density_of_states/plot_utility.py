import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

fermi_level = -0.3774

# load data
def data_loader(fname):
    data = np.loadtxt(fname)
    energy = data[:, 0] - fermi_level
    pdos = data[:, 1]  # ldos col, total contribution for a given orbital

    return energy, pdos

energy, pdos_molecule = data_loader('./molecule_summed_ldos.dat')
energy, pdos_n = data_loader('./nitrogen_summed_ldos.dat')
energy, pdos_al = data_loader('./Al_summed_ldos.dat')
energy, pdos_mgcu = data_loader('./MgCu_summed_ldos.dat')
energy, pdos_cu = data_loader('./Cu_summed_ldos.dat')
energy, pdos_al_only_n = data_loader('./Al_only_N_summed_ldos.dat')
energy, pdos_mg = data_loader('./Mg_summed_ldos.dat')
energy, pdos_total = data_loader('./Total_summed_ldos.dat')

plt.rcParams.update({'font.size': 22})
# make plots
plt.figure(figsize = (12, 12))
plt.plot(energy, pdos_molecule, linewidth=2, color='red', label="benzotriazole")
plt.plot(energy, pdos_n, linewidth=2, color='blue', label='LP N atom')
plt.plot(energy, pdos_mgcu, linewidth=2, color='green', label='MgCu bi-layer')
plt.plot(energy, pdos_al, linewidth=2, color='cyan', label='Al top layer')
# plt.plot(energy, pdos_cu, linewidth=2, color='purple', label=' Cu')
# plt.plot(energy, pdos_al_only_n, linewidth=2, color='cyan', label=' Al only N')
# plt.plot(energy, pdos_mg, linewidth=2, color='magenta', label=' Mg')
plt.plot(energy, pdos_total, linewidth=2, color='black', label='Total')

plt.yticks(visible=False)
plt.ylim(0, 90)
plt.xlim(-10, 1)
plt.xlabel('Energy (eV)')
plt.ylabel('DOS (a.u)')
plt.axvline(x= 0, linewidth=1.5, color='k', linestyle=(0, (8, 10)))
# plt.xlim(-5, 27)
# plt.ylim(0, )
# plt.fill_between(energy, 0, pdos_s, where=(energy < 7.9421), facecolor='#006699', alpha=0.25)
# plt.fill_between(energy, 0, pdos_p, where=(energy < 7.9421), facecolor='r', alpha=0.25)
# plt.fill_between(energy, 0, pdos_tot, where=(energy < 7.9421), facecolor='k', alpha=0.25)
# plt.text(6.5, 0.52, 'Fermi energy', fontsize= small, rotation=90)
# plt.grid(True)
plt.legend(frameon=False)
plt.savefig('dos.pdf')

plt.show()
