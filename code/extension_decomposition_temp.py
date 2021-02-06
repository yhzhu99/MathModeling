import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy as np

decomp=[]
extent=[]

with open('./data/decomposition_rate_temp.txt','r') as de:
    for line in de:
        x=line.split()
        decomp.append(float(x[-4])) # 10 degree
        decomp.append(float(x[-3])) # 16 degree
        decomp.append(float(x[-2])) # 22 degree
with open('./data/extension_rate_temp.txt','r') as ex:
    for line in ex:
        x=line.split()
        extent.append(float(x[-3])) # 10 degree
        extent.append(float(x[-2])) # 16 degree
        extent.append(float(x[-1])) # 22 degree

decomp_10=[decomp[i] for i in range(0,34*3,3)]
decomp_16=[decomp[i] for i in range(1,34*3,3)]
decomp_22=[decomp[i] for i in range(2,34*3,3)]
extent_10=[extent[i] for i in range(0,34*3,3)]
extent_16=[extent[i] for i in range(1,34*3,3)]
extent_22=[extent[i] for i in range(2,34*3,3)]


param = np.polyfit(extent_10, decomp_10, 1)
print(param)
p = np.poly1d(param)
coefficient_of_dermination = r2_score(decomp_10, p(extent_10))
print(coefficient_of_dermination)
plt.plot(extent_10, p(extent_10), c='blue')
plt.scatter(extent_10, decomp_10, s=150, c='blue')
plt.title('Decompostion rate-Hyphal extension rate figure (T=10degree)', fontsize=24)
plt.xlabel('Hyphal extension rate (%)', fontsize=14)
plt.ylabel('Decomposition rate (mm/day)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

param = np.polyfit(extent_16, decomp_16, 1)
print(param)
p = np.poly1d(param)
coefficient_of_dermination = r2_score(decomp_16, p(extent_16))
print(coefficient_of_dermination)
plt.plot(extent_16, p(extent_16), c='orange')
plt.scatter(extent_16, decomp_16, s=150, c='orange')
plt.title('Decompostion rate-Hyphal extension rate figure (T=16degree)', fontsize=24)
plt.xlabel('Hyphal extension rate (%)', fontsize=14)
plt.ylabel('Decomposition rate (mm/day)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

param = np.polyfit(extent_22, decomp_22, 1)
print(param)
p = np.poly1d(param)
coefficient_of_dermination = r2_score(decomp_22, p(extent_22))
print(coefficient_of_dermination)
plt.plot(extent_22, p(extent_22), c='red')
plt.scatter(extent_22, decomp_22, s=150, c='red')
plt.title('Decompostion rate-Hyphal extension rate figure (T=10, 16, 22degree)', fontsize=24)
plt.xlabel('Hyphal extension rate (%)', fontsize=14)
plt.ylabel('Decomposition rate (mm/day)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()