class Solution(object):
    def hasCycle(self, head):
		# if there is a cycle, the fast and slow point will meet eventually 
		# if the fast pointer ends, means there is no cycle
		
        if not head: return False 
        
        slow, fast = head, head 
        
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            if slow == fast:
                return True 
        return False