import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("./localization_factor_2.txt")

data = data[80:160]

bands = data[:,0].astype(np.int32)
lv = np.round(data[:,1], 4)

data = np.column_stack([bands, lv])
np.savetxt("./localization_81-160.txt", data[80:160], fmt=["%d","%f"])

# assert len(bands) == 160

total = sum(lv)
print("Total: {}".format(total))

thresh = 0.10

print(bands[lv > thresh])
np.save("../selected_wfn.npy", bands[lv > thresh])

plt.rcParams.update({'font.size': 12})
plt.figure(figsize=(7,5))
plt.scatter(bands, lv, s=40)
plt.xlim(81, 160)
plt.ylim(0, 0.25)
plt.ylabel("Localization factor")
plt.xlabel("KS index")
plt.axhline(y = thresh, linewidth=2, color='red', linestyle=(0, (8, 10)))
# plt.axvline(x = 100, linewidth=3, color='red', linestyle=(0, (8, 10)))
plt.savefig('localization.pdf')
plt.show()
