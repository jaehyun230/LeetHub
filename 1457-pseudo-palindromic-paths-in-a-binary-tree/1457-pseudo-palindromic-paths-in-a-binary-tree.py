# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        self.answer = 0
        
        def is_palindrom(d) :
            count = 0
            for x in d:
                if d[x]%2 == 1:
                    count += 1
            if count <= 1:
                self.answer += 1
                
        def dfs(node, dic) :
            
            if not node :
                return
             
            if node.val not in dic :
                dic[node.val] = 1
            else :
                dic[node.val] +=1
            
            if not node.left and not node.right :
                if is_palindrom(dic) :
                    self.answer +=1
                    dic[node.val] -=1
            
            if node.left :
                dfs(node.left, dic) 
            if node.right :
                dfs(node.right, dic)
                
            dic[node.val] -=1
            
        if root :
            dfs(root, {})
        
        return self.answer

            
            