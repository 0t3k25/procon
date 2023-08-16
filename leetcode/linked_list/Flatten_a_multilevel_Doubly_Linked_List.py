"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        self.flatten_recursively(head)
        return head

    def flatten_recursively(self, curr):
        while curr:
            # 子ノードが存在する場合
            if curr.child:
                # childのリストの最後のノードを取得
                tail = self.flatten_recursively(curr.child)

                # curr.childとcurr.nextの間に子ノードからのリストを挿入
                tail.next = curr.next
                if curr.next:
                    curr.next.prev = tail

                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

            # もしcurr.nextがnullならば、currは最後のノードなのでそれを返します。
            if not curr.next:
                return curr

            curr = curr.next
