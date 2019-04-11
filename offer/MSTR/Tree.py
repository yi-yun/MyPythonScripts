

class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None


def isPresent(root, val):
    # write your code here
    # return 1 or 0 depending on whether the element is present in the tree or not
    temp = root
    while temp:
        if val == temp.val:
            return temp
        if val > temp.value:
            temp = temp.right
        else:
            temp = temp.left
