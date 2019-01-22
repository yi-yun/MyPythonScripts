class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low <= high:
            mid=(low+high)//2
            if nums[low] == target:
                return low
            if nums[high] == target:
                return high
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
            
            
# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(Solution().search(nums,target))