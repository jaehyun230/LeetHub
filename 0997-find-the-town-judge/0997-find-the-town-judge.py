class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if len(trust)==0 and n==1:
            return 1
        dp=[0]*(n+1)
        for i in trust:
            dp[i[0]]-=1
            dp[i[1]]+=1
        for i in range(len(dp)):
            if dp[i]==n-1:
                return i
        return -1        