# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.answer = ""
        
        print(root)
        def dfs(node) :
            if not node :
                return
            self.answer +='('
            self.answer +=str(node.val)
            dfs(node.left)
            if node.left == None and node.right :
                self.answer +='()'
            dfs(node.right)
            self.answer +=')'
            
        
        dfs(root)
        
        self.answer = self.answer[1:-1]
        
        return self.answer