# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.answer = 0
        
        def search_node(node) :
            if not node :
                return
            if low <= node.val <= high :
                self.answer +=node.val
            
            if node.left :
                search_node(node.left)
            if node.right :
                search_node(node.right)
        
        
        search_node(root)
        
        return self.answer