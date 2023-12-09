# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        
        
        def findtree(node, answer) :
            
            if node.left :
                findtree(node.left, answer)
            
            answer.append(node.val)
            
            if node.right :
                findtree(node.right, answer)
            
            
        
        if root :
            findtree(root, answer)
        
        
        
        return answer