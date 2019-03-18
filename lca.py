class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # 二叉树遍历
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    # 带父节点的话 用 hashtable 存
    def LCA(self, root, p, q):
        vis = set()
        while p or q:
            if p:
                if p in vis:
                    return p
                vis.add(p)
                p = p.parent
            if q:
                if q in vis:
                    return q
                vis.add(q)
                q = q.parent
        return None
