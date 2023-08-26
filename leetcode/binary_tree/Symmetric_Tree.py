# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_node = root.left
        right_node = root.right

        def helper(left_node, right_node) -> bool:
            if left_node is None and right_node is None:
                return True
            elif left_node is None and right_node is not None:
                return False
            elif left_node is not None and right_node is None:
                return False

            if left_node.val == right_node.val:
                return helper(left_node.left, right_node.right) and helper(
                    left_node.right, right_node.left
                )
            else:
                return False

        return helper(left_node, right_node)
