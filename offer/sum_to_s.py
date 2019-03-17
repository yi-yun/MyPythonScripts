def sum_to_s(nums, s):
    low, high = 0, len(nums) - 1
    while low <= high:
        a, b = nums[low], nums[high]
        if a + b < s:
            low += 1
        elif a + b > s:
            high -= 1
        else:
            return [a, b]
    return None


def sum_to_s2(s):
    a, b = 1, 2
    ret = []
    while a < s // 2 + 1:
        if sum(range(a, b+1)) == s:
            ret.append(range(a, b + 1))
            a += 1
        elif sum(range(a, b + 1)) < s:
            b += 1
        else:
            a += 1
    return ret


# print(sum_to_s([1, 2, 4, 7, 11, 15], 15))


print(sum_to_s2(15))
