def insert(source):
    length = len(source)
    if length <= 1:
        return source
    for i in range(1, length):
        for j in range(i, 0, -1):
            if source[j] < source[j - 1]:
                source[j], source[j - 1] = source[j - 1], source[j]
            else:
                break

    return source


def bubblesort(source):
    # add flag to fast
    for i in range(len(source)):
        for j in range(1, len(source)-i):
            if source[j] < source[j - 1]:
                source[j], source[j - 1] = source[j - 1], source[j]
    return source


def selectionsort(source):
    for i in range(0, len(source)):
        min = source[i]
        index = i
        for j in range(i, len(source)):
            if source[j] < min:
                min = source[j]
                index = j
        source[i], source[index] = source[index], source[i]
    return source


if __name__ == "__main__":
    test_list = [4, 5, 6, 1, 3, 2]
    # print(insert(test_list))
    # print(bubblesort(test_list))
    print(selectionsort(test_list))
