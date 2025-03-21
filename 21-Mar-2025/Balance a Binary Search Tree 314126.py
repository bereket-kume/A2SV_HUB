# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_array = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            sorted_array.append(node.val)
            dfs(node.right)
        dfs(root)
        def helper(array, start, end):
            if start > end:
                return 
            
            mid = start + (end - start) // 2
            new_root = TreeNode(array[mid])
            new_root.left = helper(array, start, mid - 1)
            new_root.right = helper(array, mid + 1, end)
            return new_root
        return helper(sorted_array, 0, len(sorted_array)-1)
        