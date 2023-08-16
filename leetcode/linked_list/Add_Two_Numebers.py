# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy
        up = 0
        while l1 and l2:
            sum = l1.val + l2.val + up
            if sum >= 10:
                sum -= 10
                up = 1
            else:
                up = 0
            prev.next.val = sum
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + up
            if sum >= 10:
                sum -= 10
                up = 1
            else:
                up = 0
            prev.next.val = sum
            l1 = l1.next

        while l2:
            sum = l2.val + up
            if sum >= 10:
                sum -= 10
                up = 1
            else:
                up = 0
            prev.next.val = sum
            l2 = l2.next
        if up == 1:
            last_node = ListNode(1)
            prev.next = last_node
        return dummy.next
