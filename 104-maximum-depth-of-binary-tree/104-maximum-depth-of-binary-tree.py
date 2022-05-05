# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.dep(root, depth=0)
    
    def dep(self, root, depth):
        
        if not root: return depth
        
        return max(self.dep(root.right, depth+1), self.dep(root.left, depth+1))
        
        