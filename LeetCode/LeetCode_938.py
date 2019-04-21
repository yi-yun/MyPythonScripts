# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        # if not root:
        #     return 0
        # elif root.val in range(L, R + 1):
        #     return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        # elif root.val < L:
        #     return self.rangeSumBST(root.right, L, R)
        # else:
        #     return self.rangeSumBST(root.left, L, R)
        if not root:
            return 0
        ans = 0
        stack = [root]
        while len(stack) > 0:
            p = stack.pop()
            if p.val >= L and p.val <= R:
                ans += p.val
            if p.left is not None:
                stack.append(p.left)
            if p.right is not None:
                stack.append(p.right)
        return ans
