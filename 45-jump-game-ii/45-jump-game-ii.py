import heapq

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1 :
            return 0
        
        INF = int(1e9)
        
        dp = [INF] * len(nums)
        
        q = []
        
        heapq.heappush(q, (0, 0))
        
        while q :
            cost, now = heapq.heappop(q)
            
            for i in range (1, nums[now]+1) :
                if now+i < len(nums) and dp[now+i] > cost+1 :
                    heapq.heappush(q, (cost+1, now+i))
                    dp[now+i] = cost +1
        
        
        return dp[-1]
        
        
                
            
        