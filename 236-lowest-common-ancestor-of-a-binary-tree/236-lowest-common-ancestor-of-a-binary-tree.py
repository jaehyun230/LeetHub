# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
    
        return dfs(root, p, q)
    

def dfs(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left= dfs(root.left, p, q)
    right = dfs(root.right, p, q)
    
    if not left:
        return right
    
    elif not right:
        return left
    
    else:
        return root