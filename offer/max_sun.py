def max_sum(nums):
    ret = float("-inf")  # 负无穷
    if not nums:
        return ret
    current = 0
    for i in nums:
        if current <= 0:
            current = i
        else:
            current += i
        ret = max(current, ret)
    return ret


print(max_sum([1, -2, 3, 10, -4, 7, 2, -5]))
