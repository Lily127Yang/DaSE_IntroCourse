import time


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
number = {}
for line in f1:
    line = line.strip()
    list[i] = line
    i = i+1
peo_num = len(list)-1
for j in range(1, len(list)):
    list_stu[j] = list[j].split(",")
    list_stu[j] = aver(list_stu[j], 3)
my = {'10381': 'stu_A', '10382': 'stu_B', '10383': 'stu_C', '10384': 'stu_D', '10385': 'stu_E'}
f2 = open('my.txt', 'w')
for key, value in my.items():
    s = key + ':' + '' + str(value) + ' '
    f2.write(s)
f2.write('\n')
for i in range(1, 6):
    f2.write(str(format(list_stu[i], '.2f')) + ',' + ' ')
f2.write('\n')
f2.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(2)
f2.write('\n')
f2.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
f2.close