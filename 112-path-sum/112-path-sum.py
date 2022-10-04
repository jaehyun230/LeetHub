# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.answer = False
        
        def dfs(node, total) :
            if not node :
                return
            if not node.left and not node.right :
                if total + node.val == targetSum :
                    self.answer = True
            
            if node.left :
                dfs(node.left, total+node.val)
            if node.right :
                dfs(node.right, total+node.val)
        
        dfs(root, 0)
        
        
        return self.answer