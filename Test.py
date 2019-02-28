def test(target):
    i = target[0]
    i, target[i] = target[i], i
    return target


def test1(source):
    dic = {}


print(test([2, 0, 1]))
