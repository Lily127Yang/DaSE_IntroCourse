def frac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*frac(n-1)


result_list = []  # test function(frac)
for i in range(15):
    result_list.append(frac(i))
print(result_list)
