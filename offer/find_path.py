def find_path(tree, num):
    if not tree:
        return None
    ret = []
    path = [tree]
    sums = [tree]

    def dfs(tree):
        if tree.left:
            path.append(tree.left)
            sums.append(sums[-1] + tree.left.value)
            dfs(tree.left)
        if tree.right:
            path.append(tree.right)
            sums.append(sums[-1] + tree.right.value)
            dfs(tree.right)
        if not tree.left and not tree.right:
            if sums[-1] == num:
                ret.append([p.value for p in path])
            sums.pop()
            path.pop()
    dfs(tree)
    return ret
