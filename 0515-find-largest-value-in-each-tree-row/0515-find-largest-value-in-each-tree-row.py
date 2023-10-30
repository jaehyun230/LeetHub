# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        if not root: 
            return result
        
        queue = [root]
        
        while queue:
            LargestValue = float('-inf')
            
            for i in range(len(queue)):
                node = queue.pop(0)
                LargestValue = max(LargestValue, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(LargestValue)
        
        return result