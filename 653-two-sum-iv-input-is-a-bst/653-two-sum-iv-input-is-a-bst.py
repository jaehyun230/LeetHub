# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.dic = {}
        self.result = False
        
        def dfs(node) :
            if not node :
                return
            if k - node.val in self.dic :
                self.result = True
            if node.val not in self.dic :
                self.dic[node.val] = 1
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        return self.result