import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    source = list(line.split(","))
    # print(source)
    flag = False
    for i in source:
        cnt = source.count(i)
        if cnt > 1:
            flag = True
            break
    print(flag)
