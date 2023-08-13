# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_node = curr.next
            if curr.val == val:
                if prev:
                    prev.next = next_node
                else:
                    head = next_node
                curr = next_node
            else:
                prev = curr
                curr = curr.next
        return head
