import random
import math


S = 1*13
N = 10000000
count = 0
for i in range(N):
    x = random.uniform(2.0, 3.0)
    y = random.uniform(0, 13)
    if y <= pow(x, 2)+4*x*(math.sin(x)):
        count = count+1
result = S*(count/N)
print(result)

