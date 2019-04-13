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
    m, n = map(int, sys.stdin.readline().strip().split(","))
    cnt_sum = 999999

    def dfs(source, target, cnt, cnt_sum):
        if source > target + 1:
            return
        if source * 2 == target or source + 1 == target or source - 1 == target:
            cnt += 1
            cnt_sum = min(cnt_sum, cnt)
            return
        dfs(source + 1, target, cnt + 1, cnt_sum)
        dfs(source - 1, target, cnt + 1, cnt_sum)
        dfs(source * 2, target, cnt + 1, cnt_sum)

    dfs(m, n, 0, cnt_sum)
    print(cnt_sum)

    # printmul_add(3, 11)
    # cnt = 0
    # while m < n:
    #     m = m << 1
    #     cnt += 1
    # print(m)
    # print(cnt+n % m)
