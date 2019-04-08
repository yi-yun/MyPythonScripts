import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    source = list(map(int, line[1:-1].split(",")))
    n = int(sys.stdin.readline().strip())

    index = 0
    length = len(source)
    s = length // n
    res = []
    for i in range(s):
        a = source[i * n: i * n + n]
        a.reverse()
        res += a
    res += source[s * n:]
    res_str = str('[')+str(res[0])
    # res_str = '['
    for i in range(1, len(res)):
        res_str += ','
        res_str += str(res[i])

    res_str += ']'
    print(res_str)
    # print(source[i * n: i * n + n])
    # print(source)
