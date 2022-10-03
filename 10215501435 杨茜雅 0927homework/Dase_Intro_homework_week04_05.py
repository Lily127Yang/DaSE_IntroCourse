import random
import math


S = 1*2
N = 10000000
count = 0
for i in range(N):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0, 2)
    if y <= pow(x, 2)+pow(x, 3):
        count = count+1
result = S*(count/N)
print(result)