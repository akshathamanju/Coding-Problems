class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.value < root.value > q.value:
                root = root.left
            elif p.value > root.value < q.value:
                root = root.right
            else:
                return root



root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 8