# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # start from root compare p and q's val to it
        cur = root
        
        while cur:
            # if both less than move cur to left node
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # if both greater than move cur to right node
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # else, either one is equal to cur 
            # or one lesser and one greater
            # either way return it
            else:
                return cur

                