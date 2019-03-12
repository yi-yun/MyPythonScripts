class BinNode():
    def __init__(self, val):
        self.lchild = None
        self.rchild = None
        self.val = val


# 非递归
def preOrder(self, root):
    if not root:
        return
    myStack = []
    node = root
    while node or myStack:
        while node:
            print(node.val)
            myStack.append(node)
            node = node.lchild
        node = myStack.pop()
        node = node.rchild


def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = list()
    if root == None:
        return result
    stack = list()
    stack.append(root)
    while len(stack) != 0:
        top = stack.pop()
        if top.right != None:
            stack.append(top.right)
        if top.left != None:
            stack.append(top.left)
        result.append(top.val)
    return result
