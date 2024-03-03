# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        
        answer = ListNode(0)
        answer.next = head
        
        #check node length
        start = answer
        #find delete node
        find = answer
        #node length
        count = 0
        while start :
            start = start.next
            count +=1
        while count > n+1 :
            find = find.next
            count -=1
        #n node delete
        find.next = find.next.next
        
            
        return answer.next