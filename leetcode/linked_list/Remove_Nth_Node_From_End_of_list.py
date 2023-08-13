# 2つのポインタを使用: リンクリストをトラバースするために2つのポインタを使用する考え方を「2ポインタテクニック」と呼びます。

# 先行するポインタ: 1つ目のポインタをn+1ステップ進めます。

# 共に移動: その後、1つ目と2つ目のポインタをともに1ステップずつ前進させます。1つ目のポインタがリストの終わりに到達すると、2つ目のポインタは末尾からn番目のノードの一つ前に位置します。


# ノードを削除: 2つ目のポインタを使って、次のノード（末尾からn番目のノード）をリンクリストから削除します。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        # 先行するポインタをn+1ステップ進める
        for _ in range(n + 1):
            fast = fast.next

        # 共に1ステップずつ移動
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
