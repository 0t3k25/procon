# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        tempA, tempB = headA, headB

        while tempA:
            lenA += 1
            tempA = tempA.next

        while tempB:
            lenB += 1
            tempB = tempB.next

        if not lenA or not lenB:
            return None

        list_A, list_B = headA, headB

        difference = abs(lenA - lenB)
        if difference and lenA > lenB:
            for _ in range(difference):
                list_A = list_A.next
        elif difference and lenA < lenB:
            for _ in range(difference):
                list_B = list_B.next

        if list_A == list_B:
            return list_A
        while list_A and list_A.next:
            list_A = list_A.next
            list_B = list_B.next
            if list_A == list_B:
                return list_A
        return None
