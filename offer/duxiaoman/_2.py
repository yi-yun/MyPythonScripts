def fun(n, source):
    pro, cnt = 0, 0
    a = []
    for i in range(n - 1):
        temp = source[i + 1] - source[i]
        # a.append(temp)
        # print(temp)
        if temp > 0:
            pro += temp
            a.append(temp)
        else:
            # print(a)
            if len(a) >= 1:
                cnt += 1
            a = []
        if i == n - 2 and temp > 0:
            cnt += 1
    return pro, cnt*2


if __name__ == "__main__":
    # n = int(input().strip())
    # data = list(map(int, input().strip().split()))
    # pro, cnt = fun(n, data)
    a = [9, 7, 10, 11, 12, 1, 5, 6, 2]
    pro, cnt = fun(len(a), a)
    print(pro, cnt)
