"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
time = vertices + edges
space = vertices
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new = {}

        def dfs(node):
            if node in old_new:
                return old_new[node]

            # create the old and new node for hash
            old_new[node] = Node(node.val)
            for nei in node.neighbors:
                old_new[node].neighbors.append(dfs(nei))
            return old_new[node]

        return dfs(node) if node else None