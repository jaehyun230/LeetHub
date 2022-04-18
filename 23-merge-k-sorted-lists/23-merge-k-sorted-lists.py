# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        number = []
        #리스트안의 노드들
        for node in lists :
            while node :
                number.append(node.val)
                node = node.next
        #모은 숫자 정렬
        number.sort(reverse=True)
        
        #링크드 리스트 생성
        linked_list=None
        for num in number:  
            curNode=ListNode(num,linked_list)
            linked_list=curNode
                
        return linked_list
        