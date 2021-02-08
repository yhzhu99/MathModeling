import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy as np
from data_loader import load_data

extent_10, decomp_10=load_data(10)
param = np.polyfit(extent_10, decomp_10, 1)
print(param)
p = np.poly1d(param)
coefficient_of_dermination = r2_score(decomp_10, p(extent_10))
print(coefficient_of_dermination)
plt.plot(extent_10, p(extent_10), c='blue', label='T=10 degree')
plt.scatter(extent_10, decomp_10, s=100, c='blue')

extent_16, decomp_16=load_data(16)
param = np.polyfit(extent_16, decomp_16, 1)
print(param)
p = np.poly1d(param)
coefficient_of_dermination = r2_score(decomp_16, p(extent_16))
print(coefficient_of_dermination)
plt.plot(extent_16, p(extent_16), c='orange', label='T=16 degree')
plt.scatter(extent_16, decomp_16, s=100, c='orange')

extent_22, decomp_22=load_data(22)
param = np.polyfit(extent_22, decomp_22, 1)
print(param)
p = np.poly1d(param)
coefficient_of_dermination = r2_score(decomp_22, p(extent_22))
print(coefficient_of_dermination)
plt.plot(extent_22, p(extent_22), c='red', label='T=22 degree')
plt.scatter(extent_22, decomp_22, s=100, c='red')

plt.title('Decompostion rate-Hyphal extension rate figure', fontsize=24)
plt.xlabel('Hyphal extension rate (%)', fontsize=14)
plt.ylabel('Decomposition rate (mm/day)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.legend()
plt.show()