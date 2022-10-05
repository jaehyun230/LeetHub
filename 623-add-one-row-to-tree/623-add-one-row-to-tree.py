# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        if depth == 1:
            return TreeNode(val, root)
        
        def dfs(cur, dep):
            if not cur:
                return
            if dep == depth:
                cur.left = TreeNode(val, cur.left)
                cur.right = TreeNode(val, None, cur.right)
            else:
                dfs(cur.left, dep + 1)
                dfs(cur.right, dep + 1)
        
        dfs(root, 2)
        
        return root