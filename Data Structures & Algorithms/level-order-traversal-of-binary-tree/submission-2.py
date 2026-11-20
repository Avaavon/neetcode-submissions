# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this is a BFS !!!
        # start q a queue containing root
        q = collections.deque()
        q.append(root)
        # while q
        # its empty when we reach end of tree
        # each node checked will be added to active level list
        # we have a size calculation at start to avoid over appending/popping
        # append level to res and cont working on next level
        res = []
        while q:
            level = []
            level_size = len(q)
            
            for i in range(level_size):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            if level:
                res.append(level)
        return res

    # time: O(n)
    # space: O(n) from n/2 at last level siting in queue


