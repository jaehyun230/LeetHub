# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        start = head
        while start :
            count +=1
            start = start.next
        
        mid = count//2
        
        late = head
        
        if mid == 0 :
            return None
        
        while mid >= 0 :
            mid -=1
            if mid == 0 :
                late.next = late.next.next
            else :
                late = late.next
            
        
        return head
            
        