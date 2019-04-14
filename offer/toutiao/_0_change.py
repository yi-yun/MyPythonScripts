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
source = []


# def isok(i, j):
#     if i == 0 and j == 0:
#         if source[i + 1][j] == 0 and source[i][j + 1] == 0:
#             return False
#     elif i == 0 and j == len(source):
#         if source[i][j - 1] == 0 and source[i][j + 1] == 0 and source[i + 1][j] == 0:
#             return False
#     elif j == 0:
#         return False
#     return True
def find(i, j, cnt):

    if source[i][j] != 0:
        if source[i][j] == 2:
            return cnt
        if i in (0, len(source)) and j in (0, len(source[0])):
            find(i+1, j, cnt+1)
            find(i-1, j, cnt+1)
            find(i, j+1, cnt+1)
            find(i, j-1, cnt+1)


def deal(source):
    cnt = -1
    for i in range(len(source)):
        for j in range(len(source[i])):
            # print(i, j)
            if source[i][j] == 1:
                return find(i, j, 0)
    return cnt


if __name__ == "__main__":

    # global source
    while True:
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        # print(values)
        if len(values) == 0:
            break
        source.append(values)
    print(source)
    # print(ans)
