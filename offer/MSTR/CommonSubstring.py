def commonSubstring(a, b):
    length = len(a)
    for i in range(length):
        list_a = list(a[i])
        list_a.append(list(b[i]))
        flag = False
        for i in list_a:
            cnt = list_a.count(i)
            if cnt > 1:
                flag = True
                break
        print("YES") if flag else print("NO")


if __name__ == '__main__':
    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    commonSubstring(a, b)
