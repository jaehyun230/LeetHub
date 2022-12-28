import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        
        for pile in piles :
            heapq.heappush(heap, pile*-1)
        
        if heap :
            while k > 0 :
                now = heapq.heappop(heap) * -1
                if now%2 == 1 :
                    now = now//2+1
                else :
                    now = now//2
                print(now)
                heapq.heappush(heap, now*-1)
                k-=1
        
        return sum(heap)*-1