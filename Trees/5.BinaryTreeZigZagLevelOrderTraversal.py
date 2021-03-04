# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''In this problem we need to traverse binary tree level by level. When we see levels in binary tree, we need to think about bfs, because it is its logic: it first traverse all neighbors, before we go deeper. Here we also need to change direction on each level as well. So, algorithm is the following:

We create queue, where we first put our root.
result is to keep final result and direction, equal to 1 or -1 is direction of traverse.
Then we start to traverse level by level: if we have k elements in queue currently, we remove them all and put their children instead. We continue to do this until our queue is empty. Meanwile we form level list and then add it to result, using correct direction and change direction after.
Complexity: time complexity is O(n), where n is number of nodes in our binary tree. Space complexity is also O(n), because our result has this size in the end. If we do not count output as additional space, then it will be O(w), where w is width of tree. It can be reduces to O(1) I think if we traverse levels in different order directly, but it is just not worth it.'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''In this problem we need to traverse binary tree level by level. When we see levels in binary tree, we need to think about bfs, because it is its logic: it first traverse all neighbors, before we go deeper. Here we also need to change direction on each level as well. So, algorithm is the following:

We create queue, where we first put our root.
result is to keep final result and direction, equal to 1 or -1 is direction of traverse.
Then we start to traverse level by level: if we have k elements in queue currently, we remove them all and put their children instead. We continue to do this until our queue is empty. Meanwile we form level list and then add it to result, using correct direction and change direction after.
Complexity: time complexity is O(n), where n is number of nodes in our binary tree. Space complexity is also O(n), because our result has this size in the end. If we do not count output as additional space, then it will be O(w), where w is width of tree. It can be reduces to O(1) I think if we traverse levels in different order directly, but it is just not worth it.'''

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        result, direction = [], 1

        while queue:
            level = []  # local list to keep track of each nodes
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level[::direction])
            direction *= (-1)  # we are setting direction for each level
        return result


'''
Time Complexity: O(N), where N is the number of nodes in the tree.

We visit each node once and only once.

In addition, the insertion operation on either end of the deque takes a constant time, rather than using the array/list data structure where the inserting at the head could take the O(K) time where K is the length of the list.

Space Complexity: O(N) where N is the number of nodes in the tree.

The main memory consumption of the algorithm is the node_queue that we use for the loop, apart from the array that we use to keep the final output.

As one can see, at any given moment, the node_queue would hold the nodes that are at most across two levels. Therefore, at most, the size of the queue would be no more than 2 \cdot L2⋅L, assuming LL is the maximum number of nodes that might reside on the same level. Since we have a binary tree, the level that contains the most nodes could occur to consist all the leave nodes in a full binary tree, which is roughly L= 2​N/2	
 . As a result, we have the space complexity of N/2 =N in the worst case.
'''