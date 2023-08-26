from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        counter: int = 0

        if root:
            queue.append(root)

        result = []

        while queue:
            counter += 1
            level_length: int = len(queue)
            current_level = []

            for i in range(level_length):
                node = queue.popleft()

                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return counter


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
