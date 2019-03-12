def get_k_counts(nums, k):
    first = get_first_k(nums, k)
    last = get_last_k(nums, k)
    if first < 0 and last < 0:
        return 0
    if first < 0 or last < 0:
        return 1
    return last - first + 1


def get_first_k(nums, k):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (high - low) // 2 + low
        if nums[mid] > k:
            high = mid - 1
        elif nums[mid] < k:
            low = mid + 1
        else:
            if mid == 0 or nums[mid - 1] < k:
                return mid
            else:
                high = mid
    return - 1


def get_last_k(nums, k):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (high - low) // 2 + low
        if nums[mid] > k:
            high = mid - 1
        elif nums[mid] < k:
            low = mid + 1
        else:
            if mid == len(nums)-1 or nums[mid + 1] > k:
                return mid
            else:
                low = mid+1


print(get_first_k([4, 4, 4, 4, 4], 4))
print(get_last_k([4, 4, 4, 4, 4], 4))
