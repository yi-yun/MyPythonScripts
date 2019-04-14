# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)
import sys


def minutes_min(n, source):
    res = 0
    if n % 3 == 0:
        # 三个人一组
        source.sort()
        for i in range(n):
            if (i+1) % 3 == 0:
                res += source[i]
    elif n % 3 == 1:
        # 33322
        source.sort(reverse=True)
        for i in range(n):
            if i % 3 == 0:
                res += i
        res = 0
    else:
        # 33332
        res = 0
    return res


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        s = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        data = list(map(int, line.split()))
        # print(data)
        print(minutes_min(s, data))
