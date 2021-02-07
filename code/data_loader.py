
def load_data(tmp):
    decomp = []
    extent = []
    with open('./data/decomposition_rate_temp.txt', 'r') as de:
        for line in de:
            x = line.split()
            decomp.append(float(x[-4]))  # 10 degree
            decomp.append(float(x[-3]))  # 16 degree
            decomp.append(float(x[-2]))  # 22 degree
    with open('./data/extension_rate_temp.txt', 'r') as ex:
        for line in ex:
            x = line.split()
            extent.append(float(x[-3]))  # 10 degree
            extent.append(float(x[-2]))  # 16 degree
            extent.append(float(x[-1]))  # 22 degree
    decomp_10 = [decomp[i] for i in range(0, 34*3, 3)]
    decomp_16 = [decomp[i] for i in range(1, 34*3, 3)]
    decomp_22 = [decomp[i] for i in range(2, 34*3, 3)]
    extent_10 = [extent[i] for i in range(0, 34*3, 3)]
    extent_16 = [extent[i] for i in range(1, 34*3, 3)]
    extent_22 = [extent[i] for i in range(2, 34*3, 3)]
    if tmp == 10:
        return extent_10, decomp_10
    elif tmp == 16:
        return extent_16, decomp_16
    elif tmp == 22:
        return extent_22, decomp_22
    else:
        return 'Error!'
