# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        answer = ListNode(0)
        
        answer.next = head
        
        start = end = answer
        
        
        for i in range (n) :
            end = end.next
        
        while end.next :
            start = start.next
            end = end.next
        
        start.next = start.next.next
        
        return answer.next
        