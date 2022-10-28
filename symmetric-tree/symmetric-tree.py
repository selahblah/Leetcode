# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # return self.sol(root.left,root.right)
    
        
        def inorder(root, orient):
            if not root:
                return []
            
            l = []
            r = []
            if root.left:
                l = inorder(root.left, orient)

            if root.right:
                r = inorder(root.right, orient)
                
            if l and not r:
                r = [None]
                
            if r and not l:
                l = [None]
                    
            if orient == 'l':
                return [root.val] + l + r 
            
            if orient == 'r':
                return [root.val] + r + l
        
        left_order = inorder(root.left, orient = 'l')
        right_order = inorder(root.right, orient = 'r')
        
        return left_order == right_order
    

    """        
    def sol(self,l,r):
        if l is None and r is None: return True
        if l is None or r is None: return False
        
        return (l.val == r.val) and self.sol(l.right,r.left) and self.sol(l.left,r.right)
    """