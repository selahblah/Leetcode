# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.sol(root, float("-inf"), float("inf"))
    
    def sol(self,root,left,right):
        if not root: return True
        if root.val >= right or root.val <= left: return False
        
        return self.sol(root.left, left, root.val) and self.sol(root.right, root.val, right)