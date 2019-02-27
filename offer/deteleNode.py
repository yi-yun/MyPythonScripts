# need confirm exist
# del Tree Node


def delete_node(link, node):
    # 只有一个节点
    if link == node:
        del node
    # tail node
    if node.next is None:
        while link:
            if link.next == node:
                link.next = None
            link = link.next
    else:  # 中间节点
        temp = node.next
        node.val = temp.val
        node.next = temp.next
        del temp
