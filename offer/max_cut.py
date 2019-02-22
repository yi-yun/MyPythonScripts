def max_product1(length):
    if length < 2:
        return 0
    if length is 2:
        return 1
    if length is 3:
        return 2
    product = list(range(length+1))
    # print(product)
    # product = [0, 1, 2, 3]
    max = 0
    for i in range(4, length+1):
        for j in range(1, i // 2+1):
            temp = product[j] * product[i - j]
            if max < temp:
                max = temp
            product[i] = max

    max = product[length]
    return max


def max_product2(length):
    if length < 2:
        return 0
    if length is 2:
        return 1
    if length is 3:
        return 2
    time3 = length // 3
    if length - 3 * time3 is 1:
        time3 -= 1
    time2 = (length - 3 * time3) // 2
    # print(time2, time3)
    return (3**time3)*(2**time2)


if __name__ == "__main__":
    print(max_product1(8))
    print(max_product1(4))
    print(max_product2(8))
    print(max_product2(4))
