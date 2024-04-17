# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        result = ""
        result = self.dfs(root, "", result)
        return result

    def dfs(self, root, path, result):
        alpha = 'abcdefghijklmnopqrstuvwxyz' 
        if not root:
            return result
        path += alpha[root.val]

        if not root.left and not root.right:
            path = path[::-1]
            if result == "":
                result = path
            elif path < result:
                result = path
            return result
        
        result = self.dfs(root.left, path, result)
        result = self.dfs(root.right, path, result)
        return result