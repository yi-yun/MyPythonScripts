import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    source = str(sys.stdin.readline().strip())
    num = source.count("0")
    print(abs(n-2*num))
