import numpy as np

list_2 = np.zeros(5)
list_1 = [1, 2, 3, 4, 5]
for i in range(0, 5):
    list_2[4-i] = list_1[i]
for i in range(0, 5):
    print("%d" % (list_2[i]))
