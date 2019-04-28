def fun(n):
    n = abs(n)
    a = list(str(n))
    length = len(a)
    cnt = 0
    for i in a:
        temp = int(i)
        if temp != 0:
            if n % temp != 0:
                cnt += 1
    # print(cnt)
    if cnt == length:
        return 'S'
    elif cnt == 0:
        return 'G'
    else:
        return 'H'


if __name__ == "__main__":
    # tcase = int(input().strip())
    # for case in range(tcase):
    #     n = int(input().strip())
    #     print(fun(n))
    print(fun(0))
    print(fun(2))
    print(fun(-2204224))
    print(fun(-120))
    print(fun(-1))
    # print(fun(72))
    # print(fun(73))
    # print(fun(12))
