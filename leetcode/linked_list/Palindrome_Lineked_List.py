# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: "Optional[ListNode]") -> bool:
        if not head or not head.next:
            return True

        # リンクリストを2つの部分に分割します: slowとfastポインターを使う
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # リンクリストの後半部分を逆転させます
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 回文をチェック: 元のリンクリストの前半部分と逆転させた後半部分を比較
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next

        return True
