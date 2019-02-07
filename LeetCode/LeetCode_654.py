class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_num = max(nums)
        max_num_loc = nums.index(max_num)
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_num_loc])
        root.right = self.constructMaximumBinaryTree(nums[max_num_loc+1:])
        return root
