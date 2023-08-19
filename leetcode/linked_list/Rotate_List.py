# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # step1:get list length
        curr = head
        length: int = 1
        while curr.next:
            curr = curr.next
            length += 1

        # rotate num
        k %= length
        if k == 0:
            return head
        # find new head and new tail
        # find new tail
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        # find new head
        new_head = curr.next
        # set new tail
        curr.next = None
        # combine separate line to separate new tail
        curr = new_head
        while curr.next:
            curr = curr.next
        curr.next = head

        return new_head
