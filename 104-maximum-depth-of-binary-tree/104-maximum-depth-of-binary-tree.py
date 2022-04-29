class Solution(object):
    
    def maxDepth(self, root):
        return self.solve(root)

    def solve(self,root,depth = 0):
        if not root:
            return depth
        return max(self.solve(root.left,depth+1),self.solve(root.right,depth+1))
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        if not root:
            print ("000")
            return 0
    
        return max(self.maxDepth(root.right),self.maxDepth(root.left))+1
        """
        
        
        """
        return self.solve(root)
    
    def solve(self, root, depth=0):
        if not root:
            return depth
        return max(self.solve(root.left,depth+1),self.solve(root.right,depth+1))
        """
        
        
        
        
        