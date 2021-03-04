
#Time: O(n)
#space: O(1)
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def validate_binary_tree(self, root):
        return check_bst(root, float('-inf'), float('inf'))

def check_bst(node, left, right):
    if not node:
        return True
    if not left < node.val < right:
        return False
    return check_bst(node.left, left, node.val) and check_bst(node.right, node.val, right)




o1 = Solution()
root = [2,1,3]
print(o1.validate_binary_tree(root))