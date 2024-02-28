# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        self.answer = root.val
        self.depth = 0
        def find(node, depth) :
            if node.left :
                find(node.left, depth+1)
            elif depth > self.depth :
                self.depth = depth
                self.answer = node.val
                
            if node.right :
                find(node.right, depth+1)
            
        
        if root :
            find(root, 0)
        
        return self.answer
        