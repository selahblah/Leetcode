# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root: return root
        qu, res = deque([root]),[]

        while qu:
            size = len(qu)
            tmp=[]
            while size > 0:
                node = qu.popleft()
                tmp.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
                size -= 1

            res.append(tmp)
        return res
        
        

            
        

        
        