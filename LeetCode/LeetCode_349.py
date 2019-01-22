class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numa = set(nums1)
        numb = set(nums2)
        return list(numa.intersection(numb))


# 集合的 &
# nums1 = [1, 2, 2, 1]
# nums2 = [2,2]
nums1 = [4, 9, 5]
nums2 = [9,4,9,8,4]
print(Solution().intersection(nums1,nums2))