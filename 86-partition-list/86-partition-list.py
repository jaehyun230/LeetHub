# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        answer = tmp = ListNode(0)
        
        answer.next = head
        
        arr = []
        
        while head :
            arr.append(head)
            head = head.next
        
        for node in arr :
            if node.val < x :
                node.next = None
                tmp.next = node
                tmp = tmp.next
        
        for node in arr :
            if node.val >= x :
                node.next = None
                tmp.next = node
                tmp = tmp.next
        
        return answer.next
                
                