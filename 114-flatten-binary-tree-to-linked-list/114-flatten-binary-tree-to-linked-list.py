# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        stack = []
        
        def dfs(node) :
            if not node :
                return None
            stack.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
       
        if stack :
            stack = stack[::-1]
            stack.pop()
            root.left = None
        
        while stack :
            root.right = TreeNode(stack.pop())
            root = root.right
                