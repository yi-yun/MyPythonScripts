def last_kth(link, k):
    if link is None or k <= 0:
        return None
    fast = link
    while k-1 > 0:
        if fast is None:
            return None
        fast = fast.next
        k -= 1
    while fast:
        link = link.next
        fast = fast.next
    return link
