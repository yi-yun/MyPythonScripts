class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        


# return (sum(nums)-sum(set(nums)))//(len(nums) - len(set(nums)))

a = [1, 3, 4, 2, 2]
print(Solution().findDuplicate(a))
