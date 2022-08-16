# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.sum = 0
        self.low = low
        self.high = high
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            
            if node.val >= self.low and node.val <= self.high:
                self.sum += node.val
            
            elif node.val < self.low:
                return
            
            dfs(node.left)
            
        dfs(root)
        
        return self.sum