def test(target):
    i = target[0]
    i, target[i] = target[i], i
    return target


def testData():
    while True:
        data = input().strip()
        if data.isspace():
            print("is space")
            break
        else:
            data = list(map(int, data.split()))
            n, array = data[0], data[1:]

            sum = 0
            for i in range(n):
                sum += array[i]
            print(sum,)


def fun(source):
    dic = {}
    for i in source:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


if __name__ == "__main__":
    # testData()
    dic = fun([1, 2, 5, 3, 2])
    sorted(dic.items(), key=lambda e: e[1])
    print(dic)
