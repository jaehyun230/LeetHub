# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root:
                return
            l=dfs(root.left)
            r=dfs(root.right)
            if not l:
                root.left=None
            if not r:
                root.right=None
            if root.val==1 or l or r:
                return True
            else:
                root=None
                
        dfs(root)
        
        if root.val==0 and root.left==None and root.right==None:
            root=None
            
        return root
    