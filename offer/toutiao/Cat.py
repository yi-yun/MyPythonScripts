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
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    ret = 0
    for i in range(n):
        s = int(sys.stdin.readline().strip())
        dic = {}
        for j in range(s):
            line = sys.stdin.readline().strip()
            data = list(map(int, line.split()))
            n, array = data[0], data[1:]
            source = []
            for i in range(n):
                temp = (array[i * 2], array[i * 2 + 1])
                source.append(temp)
                if dic.get(temp):
                    dic[temp] = dic[temp] + 1
                else:
                    dic[temp] = 1

            a = dic.keys()
            for i in a:
                if not i in source:
                    dic[i] = 0
            # print(dic)

            ret = max(dic.values())
        print(ret)
