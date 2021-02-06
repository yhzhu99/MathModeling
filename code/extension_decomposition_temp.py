import matplotlib.pyplot as plt
import numpy as np

decomp=[]
extent=[]

with open('./data/decomposition_rate_temp.txt','r') as de:
    for line in de:
        x=line.split()
        decomp.append(float(x[-4])) # 10 °C
        decomp.append(float(x[-3])) # 16 °C
        decomp.append(float(x[-2])) # 22 °C
with open('./data/extension_rate_temp.txt','r') as ex:
    for line in ex:
        x=line.split()
        extent.append(float(x[-3])) # 10 °C
        extent.append(float(x[-2])) # 16 °C
        extent.append(float(x[-1])) # 22 °C

decomp_10=[decomp[i] for i in range(0,34*3,3)]
decomp_16=[decomp[i] for i in range(1,34*3,3)]
decomp_22=[decomp[i] for i in range(2,34*3,3)]
extent_10=[extent[i] for i in range(0,34*3,3)]
extent_16=[extent[i] for i in range(1,34*3,3)]
extent_22=[extent[i] for i in range(2,34*3,3)]


param = np.polyfit(extent_10, decomp_10, 1)
p = np.poly1d(param)
plt.plot(extent_10, p(extent_10), c='blue')

plt.scatter(extent_10, decomp_10, s=150, c='blue')
plt.title('Decompostion rate-Hyphal extension rate figure (T=10°C)', fontsize=24)
plt.xlabel('Hyphal extension rate (T=10°C)', fontsize=14)
plt.ylabel('Decomposition rate (T=10°C)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

param = np.polyfit(extent_16, decomp_16, 1)
p = np.poly1d(param)
plt.plot(extent_16, p(extent_16), c='orange')
plt.scatter(extent_16, decomp_16, s=150, c='orange')
plt.title('Decompostion rate-Hyphal extension rate figure (T=16°C)', fontsize=24)
plt.xlabel('Hyphal extension rate (T=16°C)', fontsize=14)
plt.ylabel('Decomposition rate (T=16°C)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

param = np.polyfit(extent_22, decomp_22, 1)
p = np.poly1d(param)
plt.plot(extent_22, p(extent_22), c='red')
plt.scatter(extent_22, decomp_22, s=150, c='red')
plt.title('Decompostion rate-Hyphal extension rate figure (T=22°C)', fontsize=24)
plt.xlabel('Hyphal extension rate (T=22°C)', fontsize=14)
plt.ylabel('Decomposition rate (T=22°C)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()