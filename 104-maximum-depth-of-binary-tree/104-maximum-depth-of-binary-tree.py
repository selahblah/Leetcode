# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        return max(self.maxDepth(root.right),self.maxDepth(root.left))+1
        
        """
        return self.solve(root)
    
    def solve(self, root, depth=0):
        if not root:
            return depth
        return max(self.solve(root.left,depth+1),self.solve(root.right,depth+1))
        """
        
        
        
        
        