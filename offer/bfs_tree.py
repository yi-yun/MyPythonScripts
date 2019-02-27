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
