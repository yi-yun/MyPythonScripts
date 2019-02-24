def reorder(nums, func):
    low, high = 0, len(nums) - 1
    while low <= high:
        while not func(nums[low]):
            low += 1
        while func(nums[high]):
            high -= 1
        if low < high:
            nums[low], nums[high] = nums[high], nums[low]
    return nums


# judge is or not even
def is_even(num):
    return (num & 1) == 0


if __name__ == "__main__":
    print(reorder([1, 2, 3, 4, 5], is_even))
