# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        answer = ListNode(0)
        answer.next = head
        
        def find(node) :
            start = 0
            while node :
                node = node.next
                start +=1
            
            return start
        
        
        count = find(head)
        
        find = answer
        while n < count :
            find = find.next
            count -=1
        
        find.next = find.next.next
        
        
        return answer.next