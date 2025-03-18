# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_successor(cur):
            cur = cur.right
            while cur and cur.left:
                cur = cur.left
            return cur
        
        def del_node(root, key):
            if not root:
                return root
            
            if root.val > key:
                root.left = del_node(root.left, key)
            elif root.val < key:
                root.right = del_node(root.right, key)
            else:
                if not root.left:
                    return root.right
                
                if not root.right:
                    return root.left
                
                successor = get_successor(root)
                root.val = successor.val
                root.right = del_node(root.right, successor.val)

            return root
        return del_node(root, key)