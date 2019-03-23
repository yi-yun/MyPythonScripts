"""
    1
   / \
  2   3
 / \   \
4   5   6
- 层次遍历顺序：[1 2 3 4 5 6]
- 前序遍历顺序：[1 2 4 5 3 6]
- 中序遍历顺序：[4 2 5 1 3 6]
- 后序遍历顺序：[4 5 2 6 3 1]
"""


class BinNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
    1
   / \
  2   3
 / \   \
4   5   6
- 前序遍历顺序：[1 2 4 5 3 6]
"""

# 非递归


def preOrder1(root):
    if not root:
        return
    myStack = []
    node = root
    while node or myStack:
        while node:
            print(node.val)
            myStack.append(node)
            node = node.left
        node = myStack.pop()
        node = node.right


def preOrder2(root):
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


"""
    1
   / \
  2   3
 / \   \
4   5   6
- 中序遍历顺序：[4 2 5 1 3 6]
"""


def inOrder(root):  # 中序
    res = []
    stack = []
    if root is None:
        return res
    cur = root
    while len(stack) != 0 or cur is not None:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        res.append(node.val)
        if node.right:
            cur = node.right
    return res
