def binary(n):  # 二分法
    low = 0
    high = n
    mid = high/2
    precision = 0.000000000001
    while abs(pow(mid, 3)-n) > precision:
        if (pow(mid, 3)) > n:
            high = mid
            mid = (low+mid)/2
        elif (pow(mid, 3)) < n:
            low = mid
            mid = (high+mid)/2
    return mid


print(binary(27))




