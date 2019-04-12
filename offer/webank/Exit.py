
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    source = [i for i in range(1, n + 1)]
    if n == 1:
        print(m)
        print(m)
    else:
        ret = str()
        del_number = m-1  # 该删除的编号
        for i in range(n-1):
            ret += str(source[del_number])+" "
            del source[del_number]
            del_number = (del_number + m - 1) % len(source)
        print(ret)
        print(source[0])
# if __name__ == "__main__":
#     n, m = map(int, input().strip().split())
#     source = [i for i in range(1, n + 1)]
#     if n == 1:
#         print(m)
#         print(m)
#     else:
#         ret = str()
#         del_number = m-1  # 该删除的编号
#         for i in range(n-1):
#             ret += str(source[del_number])
#             del source[del_number]
#             del_number = (del_number + m - 1) % len(source)
#         print(" ".join(ret))
#         print(source[0])
