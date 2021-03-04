# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, r):
        if root:
            self.traverse(root.left, r)
          
            r.append(root.val)
            self.traverse(root.right, r)