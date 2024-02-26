# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        self.answer = 10**8
        
        def find_leaf(node, depth) :
            if not node.right and not node.left :
                self.answer = min(self.answer, depth+1)
            
            else :
                if node.right :
                    find_leaf(node.right, depth+1)
                if node.left :
                    find_leaf(node.left, depth+1)
        
        if root :
            find_leaf(root, 0)
        else :
            self.answer = 0
        
        return self.answer