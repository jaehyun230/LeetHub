# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = ListNode(0, head)
        
        pre = 0
        re = {0: temp}
        while head:
            pre += head.val
            re[pre] = head
            head = head.next
        head = temp
        pre = 0
        while head:
            pre += head.val
            head.next = re[pre].next
            head = head.next
            
        return temp.next