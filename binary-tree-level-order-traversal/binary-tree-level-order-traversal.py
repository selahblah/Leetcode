# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = defaultdict(list)
        
        print(root)
        def count(root,level):
            if not root: 
                return
            # print(root)
            dic[level].append(root.val)
            if root.left:
                count(root.left, level + 1)

            if root.right:
                count(root.right, level + 1)
        
        count(root,level=0)
        ans = [thing for thing in dic.values()]
            
        return ans
            
    
        