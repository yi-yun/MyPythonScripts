class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)-1
        for i in range(length):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                # 交换nums[i]和nums[nums[i]]两个的位置
                # temp = nums[nums[i]]
                # nums[nums[i]] = nums[i]
                # nums[i] = temp
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


a = [1, 3, 4, 2, 2]
print(Solution().findDuplicate(a))
