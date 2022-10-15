def ip_address(ip):
    ip_list = ip.split(".")
    list = []
    for i in range(0, 4):
        list.append(binary(ip_list[i]))
    print(list)
    for i in range(0, 4):
        for j in range(0, 8):
            print(list[i][j], end=" ")
    return 0


# 变成二进制
def binary(item):
    temp = int(item)
    result = []
    while temp > 0:
        result.append(temp % 2)
        temp = temp//2
    while len(result) < 8:
        result.append(0)
    result.reverse()
    return result


ip_address("203.179.25.37")
