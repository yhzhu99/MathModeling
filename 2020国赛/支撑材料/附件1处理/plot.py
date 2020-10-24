import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

level = ('A', 'B', 'C', 'D')
number = [27, 38, 34, 24]

plt.bar(level, number)
plt.title('不同信用等级的企业分布')

plt.show()
