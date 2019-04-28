class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_depth(tree):
    if not tree:
        return 0
    if not tree.left and not tree.right:
        return 1
    return 1 + max(get_depth(tree.left), get_depth(tree.right))


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(get_depth(root))
