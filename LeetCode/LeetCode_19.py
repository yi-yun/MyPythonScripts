class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # fast = slow = head
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

        # Solution().removeNthFromEnd([1, 2], 1)
