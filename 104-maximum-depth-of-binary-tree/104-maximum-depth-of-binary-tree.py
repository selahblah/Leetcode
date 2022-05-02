# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.sol(root, depth=0)
    
    def sol(self, root, depth=0):
        
        if not root:
            return depth
        
        return max(self.sol(root.left, depth+1), self.sol(root.right, depth+1)) 