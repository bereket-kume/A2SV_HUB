# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def helper(root):
            if not root:
                return

            helper(root.left)
            ans.append(root.val)
            helper(root.right)
        helper(root)

        for i in range(1, len(ans)):
            if ans[i-1] >= ans[i]:
                return False
        return True