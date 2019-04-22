
def coin(coins, amount):
    if amount == 0:
        return 0
    res = [0] * (amount+1)
    res[0] = 0
    for i in range(1, amount + 1):
        j = 0
        temp = []
        while i >= coins[j]:
            temp.append(res[i - coins[j]]+1)
            j += 1
            if j >= len(coins):
                break
        if len(temp) == 0:
            return -1
        res[i] = min(temp)
    return res[amount]


coin([1, 3, 4], 6)
