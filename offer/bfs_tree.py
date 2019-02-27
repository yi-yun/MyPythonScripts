# print Tree Node
def bfs(tree):
    if not tree:
        return None
    queue = [tree]
    ret = []
    while queue:
        node = queue.pop(0)
        ret.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ret


# print Tree Node with \n
def bfs_change(tree):
    if not tree:
        return None
    queue = [tree]
    count = 1  # to print
    nextLevel = 0  # level
    ret = []
    while queue:
        node = queue.pop(0)
        print(node.val)
        count -= 1
        if count == 0:
            print("\n")
            count = nextLevel
            nextLevel = 0
        ret.append(node.val)
        if node.left:
            nextLevel += 1
            queue.append(node.left)
        if node.right:
            nextLevel += 1
            queue.append(node.right)
    return ret
