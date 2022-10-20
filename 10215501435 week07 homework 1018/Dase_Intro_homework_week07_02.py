def aver(array, n):
    y = 0
    for h in range(1, n+1):
        y = y+int(array[h])
    return y/n


f1 = open('score.txt', 'r')
list = {}
list_stu = {}
i = 0
k = 1
chinese = {}
math = {}
english = {}
number = {}
for line in f1:
    line = line.strip()
    list[i] = line
    i = i+1
peo_num = len(list)-1
for j in range(1, len(list)):
    list_stu[j] = list[j].split(",")
    number[k] = list_stu[j][0]
    chinese[k] = list_stu[j][1]
    math[k] = list_stu[j][2]
    english[k] = list_stu[j][3]
    k = k+1
print("chinese_average = %.2f" % aver(chinese, 5))
print("math_average = %.2f" % aver(math, 5))
print("english_average = %.2f" % aver(english, 5))


