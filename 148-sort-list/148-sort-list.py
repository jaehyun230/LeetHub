# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        answer = ListNode(0)
        
        answer.next = head
        q = []
        
        while head :
            heapq.heappush(q, head.val)
            head = head.next
        start = answer.next
        while q :
            value = heapq.heappop(q)
            start.val = value
            start = start.next
            
        return answer.next