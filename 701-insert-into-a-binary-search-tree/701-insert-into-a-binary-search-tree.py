# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left,val)
        else:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right,val)
        
        return root
        
        
        
        
        
        
        
        
        """
        while root:
            if root.val < val:
                root = root.right
            else:
                root = root.left
            self.insertIntoBST(root, val)
        
        return root
        """   
        