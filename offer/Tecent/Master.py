import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())

    d = list(map(int, input().strip().split()))  # wuli
    p = list(map(int, input().strip().split()))  # money
    # dict = {}
    # for i, (d, p) in enumerate((d, p)):
    #     dict[i] = (d, p)

    if n == 1:
        print(p[0])
    money = 0
    money += p[0]

    dp = [False] * n
    dp[0] = True  # master state

    master = 0
    master += d[0]  # cur wuli

    sumWuli = [sum(d[: i + 1]) for i in range(1, n)]

    for i in range(1, n):
        # print(master)
        if master < d[i] and sum(dp[:i]) == i:  # buy
            money += p[i]
            dp[i] = True
            master += d[i]
        elif sum(dp[:i]) != i:
            if sumWuli[i - 1] < dp[i]:
                money += p[i]
                dp[i] = True
                master += d[i]
    print(money)
