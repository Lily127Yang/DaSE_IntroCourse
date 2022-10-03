def binary_coin(coins, start, end):
    mid = (start + end) // 2
    if start == end:
        return end
    while start < end-1:
        sum1 = sum(coins[start:mid+1])
        sum2 = sum(coins[mid + 1:end+1])
        if sum1 != 2*(mid-start+1):
            end = mid
            mid = (start+end)//2
        elif sum2 != 2*(end-mid):
            start = mid
            mid = (start+end)//2
    if coins[start] == 1:
        return start
    else:
        return end


coins = [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2]
print(binary_coin(coins, 0, len(coins) - 1))
