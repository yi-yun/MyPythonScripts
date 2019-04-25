def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def test(dic):
    # for i in dic.values():
    #     if i < 1:
    #         return 0
    sorted(dic.items(), key=lambda e: e[1], reverse=False)
    list1 = []
    for i in dic.values():
        list1.append(i)
    if len(list1) == 1:
        return 1
    tmp = list1[0]

    cnt = 0
    a = gcd(tmp, list1[1])
    for i in list1:
        # if a==1:
        #     return 0
        a = gcd(a, i)
        if a == 1:
            return 0
        else:
            cnt += i//a
    return cnt


if __name__ == "__main__":
    tcase = int(input().strip())
    data = list(map(int, input().strip().split()))
    dic = {}
    for i in data:
        if i not in dic.keys():
            dic[i] = data.count(i)
    print(test(dic))
    # a=gcd(5,5)
    # print(a)
    # print(dic)
