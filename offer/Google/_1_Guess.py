# import sys


# def readline_two_int():
#     s = input()
#     a = s.split(" ")
#     return int(a[0]), int(a[1])


# if __name__ == "__main__":
#     t = int(input())
#     a, b = readline_two_int()
#     while t:
#         # print(n)
#         n = int(input())
#         while n:
#             temp = int(input())
#             if temp not in range(a + 1, b + 1):
#                 s = "WRONG_ANSWER"
#                 print(s)
#             else:

#                 if temp > 9:
#                     s = "TOO_BIG"
#                     sys.stdout.flush()
#                     print(s)
#                 elif temp == 9:
#                     s = "CORRECT"
#                     sys.stdout.flush()
#                     print(s)
#                     break
#                 else:
#                     s = "TOO_SMALL"
#                     sys.stdout.flush()
#                     print(s)
#             n -= 1

#         t -= 1
import sys


def read(a, b):
    m = a+(b-a)//2
    print(m)
    sys.stdout.flush()
    s = input()
    if s == "CORRECT":
        return
    elif s == "TOO_SMALL":
        a = m + 1
    else:
        b = m - 1
    read(a, b)


T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    i = int(input())
    read(a + 1, b)
