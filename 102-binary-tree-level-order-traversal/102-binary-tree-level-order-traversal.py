# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root :
            return root
        
        binary_tree = []
        q = []
        q.append(root)
              
        while q :
            parent, children = [], []
            while q :
                parent_node = q.pop(0)
                parent.append(parent_node.val)
                
                if parent_node.left :
                    children.append(parent_node.left)
                if parent_node.right :
                    children.append(parent_node.right)
            binary_tree.append(parent)
            q = children
        
        return binary_tree
        