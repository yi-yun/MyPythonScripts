# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        flag = False  # 默认没有还
        if not fast:
            return None 
        if not fast.next:
            return None
        # 先判断有没有环
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if flag:
            p = head
            while p != fast:
                fast = fast.next
                p = p.next
            return p
        else:
            return None 