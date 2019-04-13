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
    sum = 1
    cnt = 0
    for i in range(2, n + 1):
        sum *= i
        while sum % 10 == 0:
            sum //= 10
            cnt += 1
        if sum > 100000:
            sum %= 100000
    # print(sum)
    # while sum % 10 == 0:
    #     sum //= 10
    #     cnt += 1
    print(sum % 10)
    # print(len(temp)-temp.count('0'))
