# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums, start, end):
            if start > end:
                return None
            
            mid = start + (end - start) // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums, start, mid - 1)
            root.right = helper(nums, mid + 1, end)

            return root

        return helper(nums, 0, len(nums) - 1)