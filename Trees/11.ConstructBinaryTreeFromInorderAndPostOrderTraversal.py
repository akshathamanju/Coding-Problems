'''
preorder: 1st element wil be root
ie root, left, right
Inorder: left, root, right                     3
                                            /     \
                                           9      20
                                                 /  \
                                                15  7
preorder = [3, 9, 20, 15, 7]
           root
inorder = [9, 3, 15, 20, 7]
     left<==root==========>
                  right
                  so out of [15,20,7] which is the root, left or right
                  As 3 was the root it occured 1st in preorder, in the same way
                  we know 20 is the root and 15 is the left child and 7 is the
                  right child
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # Recursive solution
        if inorder:
            # Find index of root node within in-order traversal
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])

            # Recursively generate left subtree starting from
            # 0th index to root index within in-order traversal
            root.left = self.buildTree(preorder, inorder[:index])

            # Recursively generate right subtree starting from
            # next of root index till last index
            root.right = self.buildTree(preorder, inorder[index + 1:])
            return root