import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        result = []
        
        q = []
        
        for num in arr :
            heapq.heappush(q, (abs(x-num), num))
        
        for i in range(k) :
            _ , num = heapq.heappop(q)
            result.append(num)
        
        result.sort()
        
        return result