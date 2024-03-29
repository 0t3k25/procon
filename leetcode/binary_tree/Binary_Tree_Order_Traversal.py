from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()

        if root:
            queue.append(root)

        result = []

        while queue:
            level_length = len(queue)
            current_level = []

            for i in range(level_length):
                node = queue.popleft()

                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result
