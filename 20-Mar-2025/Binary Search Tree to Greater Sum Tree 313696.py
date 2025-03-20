# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node, current_sum):
            if not node:
                return current_sum
            
            right = helper(node.right, current_sum)
            node.val += right
            left = helper(node.left, node.val)
            return left
        helper(root, 0)
        return root