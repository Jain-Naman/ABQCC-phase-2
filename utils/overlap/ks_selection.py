import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

'''
state #  29: atom  11 (N  ), wfc  1 (l=0 m= 1)
state #  30: atom  11 (N  ), wfc  2 (l=1 m= 1)
state #  31: atom  11 (N  ), wfc  2 (l=1 m= 2)
state #  32: atom  11 (N  ), wfc  2 (l=1 m= 3)
state #  33: atom  12 (N  ), wfc  1 (l=0 m= 1)
state #  34: atom  12 (N  ), wfc  2 (l=1 m= 1)
state #  35: atom  12 (N  ), wfc  2 (l=1 m= 2)
state #  36: atom  12 (N  ), wfc  2 (l=1 m= 3)
### state #  37: atom  13 (H  ), wfc  1 (l=0 m= 1)
state #  38: atom  14 (N  ), wfc  1 (l=0 m= 1)
state #  39: atom  14 (N  ), wfc  2 (l=1 m= 1)
state #  40: atom  14 (N  ), wfc  2 (l=1 m= 2)
state #  41: atom  14 (N  ), wfc  2 (l=1 m= 3)

state #  54: atom  18 (Al ), wfc  1 (l=0 m= 1)
state #  55: atom  18 (Al ), wfc  2 (l=1 m= 1)
state #  56: atom  18 (Al ), wfc  2 (l=1 m= 2)
state #  57: atom  18 (Al ), wfc  2 (l=1 m= 3)
'''

# n_orbitals = [29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41] + [54, 55, 56, 57] + list(range(74, 110))
n_orbitals = [29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41]

# Select wavefns above threshold 
localized_wfn = np.load("./selected_wfn.npy").astype(int)
print(localized_wfn)

ks_proj = np.load("../test/data_matrix.npy")

# select particular wavefunctions
selected_wfn = ks_proj[:,localized_wfn - 1]

subspace = selected_wfn[n_orbitals]

squared_coeff = np.apply_along_axis(lambda x: x**2, 0, subspace)

overlap = np.sum(squared_coeff, axis=0)
overlap = np.sqrt(overlap)

index = 0
for l in localized_wfn:
    print("Index: {}".format(index), l, overlap[index])
    index += 1

plt.rcParams.update({'font.size': 12})

c1 = patches.Ellipse((localized_wfn[13], overlap[13]), width=5, height=0.01, color='r', fill = False, linewidth=2)
c2 = patches.Ellipse((localized_wfn[19], overlap[19]), width=5, height=0.01, color='r', fill = False, linewidth=2)
c3 = patches.Ellipse((localized_wfn[20], overlap[20]), width=5, height=0.01, color='r', fill = False, linewidth=2)
c4 = patches.Ellipse((localized_wfn[21], overlap[21]), width=5, height=0.01, color='r', fill = False, linewidth=2)
c5 = patches.Ellipse((localized_wfn[22], overlap[22]), width=5, height=0.01, color='r', fill = False, linewidth=2)

plt.scatter(localized_wfn, overlap, s=30, marker='D', c="blue")
plt.ylabel("Overlap")
plt.xlabel("KS index")
plt.axhline(y = 0.0250, linewidth=2, color='orange', linestyle=(0, (8, 10)))
plt.gca().add_patch(c1)
plt.gca().add_patch(c2)
plt.gca().add_patch(c3)
plt.gca().add_patch(c4)
plt.gca().add_patch(c5)

plt.savefig('localized_wfn-overlap-3N.pdf')
plt.show()