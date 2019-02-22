import sys


def tail_recursion(n, total=0):
    if n == 0:
        return total
    else:
        return tail_recursion(n-1, total+n)


if __name__ == "__main__":
    sys.setrecursionlimit = 1003
    print(tail_recursion(999))
