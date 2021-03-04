# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
use queue for storing the elements
for each element in the queue check whether thay have children

Time: O(n)
space: O(n)
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #print(root)
        #if Root is None i.e there are no nodes
        # then return empty list
        if root == None:
            return []

        #add the root value in the result list
        res = [[root.val]]
        #store the root in queue
        queue = [root]

        #while queue length is greater than zero traverse
        while len(queue) > 0:

            #temp stores the pointer to left and right child
            temp = []
            #value list stores the value of left and right child of current node
            value = []

            #for the available nodes in the queue
            for node in queue:
                #if there's a left node then store the pointer and value in the list
                if node.left:
                    temp.append(node.left)
                    value.append(node.left.val)
                #similarly for the right child
                if node.right:
                    temp.append(node.right)
                    value.append(node.right.val)
            #now update the queue to traverse next level
            queue = temp
            #if value is not empty then append the value to result list
            if value:
                res.append(value)

        #finally return the result list
        return res