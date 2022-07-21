# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value = []
        
        curr = head
        result = head
        
        while curr !=None :
            value.append(curr.val)
            curr = curr.next
            
        while head :
            head.val = value.pop()
            head = head.next
            
        
        return result