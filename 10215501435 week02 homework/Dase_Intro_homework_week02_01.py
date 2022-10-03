height = float(input("请输入你的身高(米）："))
weight = float(input("请输入你的体重（千克）： "))
print('你的身高和体重是：%.2f米 %.2f千克.' % (height, weight))
bmi = weight/(height**2)
if bmi < 18.5:
    print('您的bmi指数是：%.2f。太轻啦！多吃点多吃点！' % bmi)
elif 18.5 <= bmi < 24:
    print('您的bmi指数是：%.2f。正常噢，继续保持！' % bmi)
elif 24 <= bmi < 28:
    print('您的bmi指数是：%.2f。超重喽！减减肥叭~' % bmi)
elif 28 <= bmi:
    print('您的bmi指数是：%.2f。肥胖肥胖！' % bmi)





