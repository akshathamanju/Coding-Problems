from collections import deque

class Solution:
    def connect(self, root):
        if not root:
            return root
        parent = head
        childHead = None
        child = None

        while parent:
            while parent:
                if parent.left != None:
                    if childHead == None:
                        childHead = parent.left
                    else:
                        child.next = parent.left

                    child = parent.left
                if parent.right != None:
                    if childHead == None:
                        childHead = parent.right
                    else:
                        child.next = parent.right
                    child = parent.right
                parent = parent.next
            parent = childHead
            childHead = child = None



