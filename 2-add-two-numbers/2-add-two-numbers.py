# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_val = 0
        l2_val = 0
        
        num = 1
        while l1:
            l1_val +=l1.val*num
            l1=l1.next
            num *=10
        
        num = 1
        while l2:
            l2_val +=l2.val*num
            l2=l2.next
            num *=10
        
        out_val = l1_val+l2_val
        
        header=None
        linked_list=None
        for c in str(out_val):
            if not header:
                header=ListNode(int(c))
                linked_list=header
            else:
                curNode=ListNode(int(c),linked_list)
                linked_list=curNode
            
        
        return linked_list