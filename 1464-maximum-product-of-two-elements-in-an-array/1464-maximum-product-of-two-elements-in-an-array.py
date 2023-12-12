import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        q = []
        
        for num in nums :
            heapq.heappush(q, -num) 
        
        answer = 1
        
        for i in range(2) :
            val = heapq.heappop(q)
            val *=-1
            answer *=(val-1)
        
        return answer