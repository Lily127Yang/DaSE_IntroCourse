# 通过二分法求n的三次方根的值
def cube_root(n):
    temp = n
    precision = 0.0000001
    low = 0
    high = temp / 2
    while abs(pow(high, 3) - temp) > precision:
        if (pow(high, 3)) > temp:
            high = (high + low) / 2
        elif (pow(high, 3)) < temp:
            x = high + (high - low) / 2
            low = high
            high = x
        else:
            return high
        print(high)


if __name__ == "__main__":
    cube_root(12)