# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num = root.val
        self.answer = 0
        
        def binary_search(node, value):
            
            if not node :
                return
            
            if node.val >= value :
                self.answer +=1
                value = node.val
                           
            if node.left :
                binary_search(node.left, value)
            if node.right :
                binary_search(node.right, value)
            
            return
        
        binary_search(root, -10**4)
        
        return self.answer