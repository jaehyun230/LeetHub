import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        q=[]
        
        answer=0
        totalspeed=0
        
        arr = []
        for i in range (n) :
            arr.append([efficiency[i], speed[i]])
        arr.sort(key=lambda x:-x[0])
        
        for eff, sp in arr:
            heapq.heappush(q, sp)
            totalspeed +=sp
            
            if len(q) > k:
                totalspeed -= heapq.heappop(q)
            
            answer = max(answer,totalspeed*(eff))
        
        
        return answer%(10**9+7)