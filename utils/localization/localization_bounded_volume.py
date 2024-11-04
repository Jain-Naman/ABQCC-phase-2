import numpy as np

# FFT dimensions: ( 135, 150, 625)
#   celldm(1)   = 15.05421972,
#   celldm(2)   = 1.156499525,
#   celldm(3)   = 4.75

# dV = del x * del y * del z

# Total volume - 

Lx = 15.05421972
Ly = 17.4101979554
Lz = 71.50754367
nx = 135
ny = 150
nz = 625

print("Total volume: {}".format(Lx*Ly*Lz))

del_x = Lx/nx
del_y = Ly/ny
del_z = Lz/nz
# Lx =  15.05421972, Ly = 17.4101979554, Lz = 71.50754367

dV = (del_x)*(del_y)*(del_z) # Dense grid

b_factor = 1.88973

x_min, x_max = (1.5*b_factor, 6.5*b_factor)
y_min, y_max = (0, 5.5*b_factor)
z_min, z_max = (1*b_factor, 6*b_factor)

region = [x_min/del_x, x_max/del_x, y_min/del_y, y_max/del_y, z_min/del_z, z_max/del_z]
region_gp = [round(e) for e in region]

print("Volume element: {}".format(dV))

for b in range(100, 126):
    band = b

    psi_sq = np.loadtxt('MgAl2Cu_plot.dat_K001_B{}'.format(band), skiprows=70)
    psi_sq = psi_sq.reshape((nz, ny, nx))
    psi_sq_region = psi_sq[region_gp[4]:region_gp[5], region_gp[2]:region_gp[3], region_gp[0]:region_gp[1]]

    psi_sq_region = psi_sq_region.reshape(-1)
    lv = (np.sum(psi_sq_region)*dV)

    print(lv)
    localization_factor = lv

    with open("./localization_factor.txt", "a") as f:
        f.write("{} {}\n".format(band, localization_factor))

    print("Band {} - LF: {}\n".format(band, localization_factor))
