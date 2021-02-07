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
plt.plot(extent_10, p(extent_10), c='red')
plt.scatter(extent_10, decomp_10, s=100, c='blue')
plt.title('Decompostion rate-Hyphal extension rate figure', fontsize=24)
plt.xlabel('Hyphal extension rate (%)', fontsize=14)
plt.ylabel('Decomposition rate (mm/day)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()