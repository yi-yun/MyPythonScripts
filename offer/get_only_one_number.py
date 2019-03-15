def get_only_one_number(nums):
    if not nums:
        return None
    temp = 0
    for n in nums:
        temp ^= n
    last_one = get_bin(temp)
    a_ret, b_ret = 0, 0
    for n in nums:
        if is_one(n, last_one):
            a_ret ^= n
        else:
            b_ret ^= n
    return [a_ret, b_ret]


def get_bin(num):  # 得到第一个1
    ret = 0
    while num & 1 == 0 and ret < 32:
        num = num >> 1
        ret += 1
    return ret


def is_one(num, t):  # 验证t位是不是1
    num = num >> t
    return num & 0x01


# print(get_bin(12))
# print(get_bin(11))
# print(get_bin(2))
print(get_only_one_number([2, 4, 3, 6, 3, 2, 5, 5]))
