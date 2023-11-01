# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        m = {}
        def dfs(tree):
            
            if not tree:
                return
            
            if tree.val in m:
                m[tree.val] += 1
            else:
                m[tree.val] = 1
            
            dfs(tree.left)
            dfs(tree.right)
        
        dfs(root)
        mx = max(m.values())
        return [i for i in m if m[i] == mx]