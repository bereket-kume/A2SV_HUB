# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, s):
            if not node:
                return False
            
            s += node.val
            if node.left is None and node.right is None and targetSum == s:
                return True
            
            return dfs(node.left, s) or dfs(node.right, s)
            
        return dfs(root, 0)