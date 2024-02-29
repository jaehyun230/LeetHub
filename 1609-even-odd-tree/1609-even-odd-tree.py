# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode], depth = 0) -> bool:
        
        pre_depth = 0
        pre_value = float('-inf')
        q = deque()
        q.append([root, pre_depth])
        
        while q :
            now, depth = q.popleft()
            
            if depth%2 == 0 :
                if now.val %2 == 0 :
                    return False
            
                if depth == pre_depth :
                    if now.val <= pre_value :
                        return False
            
            elif depth%2 == 1 :
                if now.val %2 == 1 :
                    return False
                if depth == pre_depth :
                    if now.val >= pre_value :
                        return False
            
            if now.left :
                q.append([now.left, depth+1])
            if now.right :
                q.append([now.right, depth+1])
            
            pre_depth = depth
            pre_value = now.val
            
            
        return True