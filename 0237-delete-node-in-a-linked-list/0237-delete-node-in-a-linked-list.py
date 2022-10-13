# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        
        nextNodeVal = node.next.val 
        node.val = nextNodeVal
        node.next = node.next.next
        
        