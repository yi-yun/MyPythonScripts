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


if __name__ == "__main__":
    print(insert([4, 5, 6, 1, 3, 2]))
