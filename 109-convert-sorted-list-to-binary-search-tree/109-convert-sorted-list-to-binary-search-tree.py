# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        arr = []
        
        while head :
            arr.append(head.val)
            head = head.next
            
        arr.sort()
        
        def dfs(path) :
            
            if not path :
                return None
            
            mid = len(path)//2
            
            answer = TreeNode(path[mid])
            
            answer.left = dfs(path[:mid])
            answer.right = dfs(path[mid+1::])
            
            
            return answer
        
        return dfs(arr)