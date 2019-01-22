class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                return min(self.findMin(nums[:mid + 1]), self.findMin(nums[mid + 1:]))
        
        return nums[low]

print(Solution().findMin([10,1,10,10,10]))