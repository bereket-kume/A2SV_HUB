# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left, right, depth):
            if not left or not right:
                return
            if depth % 2 == 1:
                left.val, right.val = right.val, left.val
            dfs(left.left,right.right, depth + 1)
            dfs(left.right,right.left, depth + 1)
            if not root:
                return None

        dfs(root.left, root.right, 1)
        return root