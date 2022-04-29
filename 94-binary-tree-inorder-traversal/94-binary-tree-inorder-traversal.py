# Definition for a binary tree node.

class Solution(object):
    def inorderTraversal(self, root):        
        res=[]
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res