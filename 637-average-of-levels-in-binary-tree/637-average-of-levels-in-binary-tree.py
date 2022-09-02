# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dic = defaultdict(list)
        
        def search(node, depth) :
            if not node :
                return
            dic[depth].append(node.val)
            
            search(node.left, depth+1)
            search(node.right, depth+1)
        
        search(root, 0)
        result = []
        for i in dic :
            value = round(sum(dic[i])/len(dic[i]), 5)
            result.append(value)
        
        return result
        
        