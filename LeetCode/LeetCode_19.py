class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # fast ,slow =head, head
        # if n == 1 and not head.next:
        #     # print(n)
        #     return []
        # while n:
        #     if fast is None:
        #         return None
        #     fast = fast.next
        #     n = n-1
        # while fast.next:
        #     slow = slow.next
        #     fast = fast.next
        # if not slow.next:
        #     return None
        # slow.next = slow.next.next
        # return head
        if n == 1 and not head.next:
            return None
        fast, slow = head, head
        while n and fast:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        temp = slow.next.next
        del slow.next
        slow.next = temp
if __name__ == "__main__":
    head = ListNode(1)
    head.next=ListNode(2)
    Solution().removeNthFromEnd(head, 1)
    print(head.val)
