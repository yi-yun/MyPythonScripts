if __name__ == "__main__":
    n, k, m = map(int, input().strip().split())
    if 0 in (n, k, m):
        print(0)
    else:
        if n * k < m:
            print(k)
        else:
            if n * k % m == 0:
                print(n * k // m) if n * k // m > k else print(k)
            else:
                print(n * k // m+1+k)
