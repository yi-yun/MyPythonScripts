if __name__ == "__main__":
    m, n = map(int, input().strip().split())
    source = []
    dic_1 = {}
    dic_2 = {}
    for i in range(m):
        data = list(map(int, input().strip().split()))
        source.append(data)
    # print(source)
    for i in range(len(source)):
        for j in range(len(source[0])):
            if (i + j) % 2 == 0:
                if dic_1.get(source[i][j], False):
                    dic_1[source[i][j]] += 1
                else:
                    dic_1[source[i][j]] = 1
            else:
                if dic_2.get(source[i][j], False):
                    dic_2[source[i][j]] += 1
                else:
                    dic_2[source[i][j]] = 1
    sorted(dic_1.items(), key=lambda e: e[1], reverse=True)
    sorted(dic_2.items(), key=lambda e: e[1], reverse=True)
    list1 = []
    list2 = []
    for i in dic_1.items():
        list1.append(i)
    for i in dic_2.items():
        list2.append(i)
    print(list1, list2)
    a = list1[0]
    b = list2[0]
    # if a[0] != b[0]:
    #     print(m*n//2+1-a[1]+m*n//2-b[1])
    if a[0] == b[0]:
        if len(list2) > 1:
            b = list2[1]
            left = m * n - a[1] - b[1]
        else:
            left = m * n - a[1]
        if len(list1) > 1:
            a = list1[1]
            right = m*n-a[1]-b[1]
        else:
            right = m * n - b[1]
        print(left) if left < right else print(right)
    else:
        print(m * n - a[1] - b[1])
    # print(b)
    # print(m * n - a[1] - b[1])
