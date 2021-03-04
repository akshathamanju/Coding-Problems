"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        do level order traversal and set next pointers along the way
        '''
        '''
         do level order traversal and set next pointers along the way
         '''
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        # Solution using BFS
        queue = deque([root])

        while queue:
            node = queue.popleft()

            # If we have both, left and right child
            if node.left and node.right:
                # Left child's next will be right child
                node.left.next = node.right
                # If node has next, then right child's next will be node's next's left
                if node.next:
                    node.right.next = node.next.left

                # Continue BFS
                queue.append(node.left)
                queue.append(node.right)

        return root


'''
    V=number of nodes in tree
    runtime: O(V), since we are doing a BFS on a tree. level order traversal is basically a bfs in batches. BFS is O(V+E) for graphs, but in trees E=V-1, so BFS becomes O(V) for trees.
    space: O(V), since at worst case we have a full binary tree, and so we will have to store the whole bottom level in memory. the size of the tree is dominated by the bottom level. 
    '''
#optimal without using extra space
'''
without using extra space:
idea: In each of the levels we will starting from left most node,
so I will assign leftmost node as root


'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left
                head = head.next

            #moving to the next level
            leftmost = leftmost.left
        return root
