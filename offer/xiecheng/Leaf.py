import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    a = line.split(" ")
    n = a[0]
    leaf = a[1:]
    dic_list = []
    dic = {}
    for i in leaf:
        source = i.split("/")
        for index, v in enumerate(source):
            dic
