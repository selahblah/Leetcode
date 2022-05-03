# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        tem = []
        self.addvalue(root,tem)
        print(tem)
        
        if len(tem) == 1:
            return False
        
        return self.sol(root,tem,k)
    
    def sol(self, root,tem,k):
        while root:
            tem.remove(root.val)
            if k-root.val in tem:
                return True
            return self.sol(root.right,tem,k) or self.sol(root.left,tem,k)
        return False
            
    def addvalue(self, root, tem):
        while root:
            tem.append(root.val)
            return self.addvalue(root.right,tem) or self.addvalue(root.left,tem)
        
        
        
    


        