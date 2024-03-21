# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        start = ListNode()
        curr = head
        result = head
        
        stack = []
        while curr :
            stack.append(curr.val)
            curr = curr.next
        
        while head :
            now = stack.pop()
            head.val = now
            head = head.next
            
        return result