# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.answer = []
        
        def dfs(node, total, path) :
            
            if not node:
                return
            
            total = total +node.val
            path = path +[node.val]
            if not node.right and not node.left :
                if total == targetSum :
                    self.answer.append(path)
            
            dfs(node.left, total, path)
            dfs(node.right, total, path)
            
        dfs(root, 0, [])
        
        return self.answer