# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev, curr = None, head

        while curr:
            next_node = curr.next  # 次のノードを保存
            curr.next = prev  # 現在のノードのnextポインタの方向を変更
            prev = curr  # prevポインタを移動
            curr = next_node  # currポインタを移動
        return prev
