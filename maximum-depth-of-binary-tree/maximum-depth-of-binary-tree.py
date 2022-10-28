class Solution(object):
    def maxDepth(self, root):
        return self.dfs(root,depth=0)
    
    def dfs(self,root,depth):
        if not root: return depth
        return max(self.dfs(root.right,depth+1),self.dfs(root.left,depth+1))