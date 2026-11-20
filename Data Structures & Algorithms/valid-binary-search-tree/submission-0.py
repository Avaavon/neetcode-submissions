# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # create a function to take the node and its left and right range
        def valid(node, left, right):
            # if this node is none its true
            if not node:
                return True
            # if this node does not fit inside range return False
            if not (node.val > left and node.val<right) :
                return False
            
            return valid(node.left,left,node.val) and valid(node.right, node.val,right)
        return valid(root, float("-inf"),float("inf"))

    # time: O(h), O(n) if imbalanced
    # space: O(n)

        
