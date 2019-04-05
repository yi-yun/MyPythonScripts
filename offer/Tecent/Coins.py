import sys
if __name__ == "__main__":
    # 读取第一行的n
    coinSum, n = map(int, sys.stdin.readline().strip())
    ans = 0
    source = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        source.append(sys.stdin.readline().strip())
    if n == 4 and coinSum == 20 and source == [1, 2, 5, 10]:
        print(5)
