def judge(n):
    cnt = 0
    while n != 1:
        cnt += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return cnt


if __name__ == "__main__":
    t = int(input())
    data = list(map(int, input().strip().split()))
    cnt = 0
    for i in range(t):
        print(judge(data[cnt]))
        cnt += 1
