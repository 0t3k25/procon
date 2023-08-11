class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        for _ in range(index):
            if not curr:
                return -1
            curr = curr.next
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        for _ in range(index - 1):
            if not curr:
                return
            curr = curr.next
        new_node = Node(val)
        new_node.next = curr.next if curr else None
        if curr:
            curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            if curr and curr.next:
                curr.next = curr.next.next


class Node:
    def __init__(self, val: int = 0, next=None) -> None:
        self.val = val
        self.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
