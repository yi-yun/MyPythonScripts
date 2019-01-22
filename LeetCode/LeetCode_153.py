class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high=0,len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]

test=[4,5,6,7,0,1,2]
test = [3, 3, 1, 3]
test=[10,1,10,10,10]
print(Solution().findMin(test))

