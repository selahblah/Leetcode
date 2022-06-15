"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        li = defaultdict(list)
        
        def dfs(node,level):
            if not node: return
            li[level].append(node.val)
            for c in node.children:
                dfs(c, level+1)
                
        dfs(root,0)
        return [lst for k,lst in li.items()]