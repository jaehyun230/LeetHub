# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        check = []
        temp = head
        
        while temp :
            check.append(temp.val)
            temp = temp.next
        
        index = len(check) - 1
        while head :
            if head.val != check[index] :
                return False
            head = head.next
            index -=1
        
        return True