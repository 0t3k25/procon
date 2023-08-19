"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # step1:copy node in hash map
        hash_map = dict()
        current = head
        while current:
            hash_map[current] = Node(current.val)
            current = current.next

        # step2:set each node's next node and random pointer
        current = head
        while current:
            if current.next:
                hash_map[current].next = hash_map[current.next]
            if current.random:
                hash_map[current].random = hash_map[current.random]
            current = current.next
        return hash_map[head]
