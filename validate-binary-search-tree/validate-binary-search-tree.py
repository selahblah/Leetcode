# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.compare(root,float("-inf"),float("inf"))
    
    def compare(self, root, l, r):
        if not root: return True
        if root.val >= r or root.val <= l: return False
        
        return self.compare(root.left,l,root.val) and self.compare(root.right,root.val,r)
        
        