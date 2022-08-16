# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        global sum
        sum = 0

        def dfs(node) :
            global sum
            if low <= node.val <= high :
                sum +=node.val

            if node.left != None :
                dfs(node.left)
            if node.right != None :
                dfs(node.right)
        dfs(root)
        
        return sum