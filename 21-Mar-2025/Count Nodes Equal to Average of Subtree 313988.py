# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def helper(node):
            nonlocal count
            if not node:
                return (0, 0)
            left_size, left_sum = helper(node.left)
            right_size, right_sum = helper(node.right)

            total_sum = left_sum + right_sum + node.val
            size = left_size + right_size + 1

            if node.val == (total_sum // size):
                count += 1
            return (size, total_sum)
        helper(root)
        return count