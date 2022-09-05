"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import defaultdict

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        self.dic = defaultdict(list)
        
        def dfs(node, depth) :
            
            if not node :
                return
            self.dic[depth].append(node.val)
            
            if node.children :
                for child in node.children :
                    dfs(child, depth+1)
        
        dfs(root, 0)
        
        return self.dic.values()