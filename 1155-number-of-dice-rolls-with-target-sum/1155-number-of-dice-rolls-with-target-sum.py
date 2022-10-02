class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1 for j in range(target+2)] for i in range(n+1)]
        def cal(rem_d, tot_S):
            
            if rem_d == 0 and tot_S == 0:
                return 1
            
            if tot_S < 0 or rem_d <= 0:
                return 0
            
            if dp[rem_d][tot_S] != -1: return dp[rem_d][tot_S]

            ans = 0
            for a in range(1,k+1):
                ans += cal(rem_d-1, tot_S - a)
            dp[rem_d][tot_S] =  ans
            return dp[rem_d][tot_S]
        
        return cal(n, target)%(10**9+7)