import random


def more_than(nums, k):
    low, high = 0, len(nums)-1
    mid = low + (high - low) // 2
    if mid == part(nums):
        return nums[mid]


def part(nums):
    low, high = 0, len(nums)-1
    a = random.randint(low, high)
    if a != 0:
        nums[0], nums[a] = nums[a], nums[0]
    i = 0
    for j in range(1, len(nums)):
        if nums[j] <= nums[0]:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
