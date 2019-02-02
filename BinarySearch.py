# 查找第一个值等于给定值的元素
def find1(source, target):
    low, high = 0, len(source)-1
    while low <= high:
        mid = low + (high - low) // 2
        if source[mid] == target:
            if mid == 0 or source[mid - 1] != target:
                return mid
            else:
                high = mid - 1
        elif source[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 查找最后一个值等于给定值的元素
def find2(source, target):
    low, high = 0, len(source)-1
    while low <= high:
        mid = (high - low) // 2 + low
        if source[mid] < target:
            low = mid + 1
        elif source[mid] > target:
            high = mid - 1
        else:
            if mid == len(source) - 1 or source[mid + 1] != target:
                return mid
            else:
                low = mid + 1
    return -1


print(find1([1, 3, 4, 5, 6, 8, 8, 8, 11, 18], 8))
print(find2([1, 3, 8, 8, 8, 11, 18], 8))
