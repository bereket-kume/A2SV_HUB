# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        def dfs(node, depth):
            if not node:
                return
            
            if len(ans) == depth:
                ans.append([node.val])
            else:
                ans[depth].append(node.val)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        ans = [sum(i)/len(i) for i in ans]
        return ans