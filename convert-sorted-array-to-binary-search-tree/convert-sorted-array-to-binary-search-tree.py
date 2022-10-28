# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(a, b, level = 0):
            if a == b:
                print("\t"*level, None)
                return
            m = (a + b) // 2
            root = TreeNode(val = nums[m])
            print("\t"*level, root.val)
            root.left = solve(a, m, level + 1)
            root.right = solve(m + 1, b, level + 1)

            return root
            
        root = solve(0, len(nums))

        return root
        
        
        
        