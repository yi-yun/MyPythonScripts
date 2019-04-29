# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        mid = self.getMiddle(head)
        right = mid.next
        mid.next = None
        return self.merge(self.sortList(head), self.sortList(right))

    def getMiddle(self, head):
        if head is None:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, left, right):
        dummyNode = ListNode(0)
        dummyHead = dummyNode
        while left and right:
            if left.val < right.val:
                dummyHead.next = left
                left = left.next
            else:
                dummyHead.next = right
                right = right.next
            dummyHead = dummyHead.next
        if left:
            dummyHead.next = left
        elif right:
            dummyHead.next = right
        return dummyNode.next


if __name__ == "__main__":
    test = ListNode(2)
    test.next = ListNode(1)
    test.next.next = ListNode(5)
    a = Solution().sortList(test)
    print(a.val)
