class Link():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def fun(source):
    # source 原链表
    if not source:
        return None
    slow = fast = source
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
        slow = slow.next
        # 偶数判断
        if fast is None:
            return slow
        # 奇数判断
        if fast.next is None:
            return slow


if __name__ == "__main__":
    link = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    link2 = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    print(fun(link).val)
    print(fun(link2).val)
