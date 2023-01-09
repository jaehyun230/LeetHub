# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        
        def preorder(node) :
            if not node :
                return
            else :
                self.answer.append(node.val)
                
                if node.left :
                    preorder(node.left)
                if node.right :
                    preorder(node.right)
        
        preorder(root)
        
        return self.answer
                
        