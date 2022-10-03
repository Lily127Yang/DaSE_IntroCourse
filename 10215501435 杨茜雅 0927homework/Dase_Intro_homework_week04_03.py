max = 1


def count_each_char(str):
    global max
    dict = {}
    for i in str:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for i in dict:
        if dict[i] > max:
            max = dict[i]
            sign = i
    if max == 1:
        return "not found"
    return sign


if __name__ == "__main__":
    res = count_each_char("aabbccddeefff")
    for i in range(0, max):
        print(res, end="")





