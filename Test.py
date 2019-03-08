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


testData()
