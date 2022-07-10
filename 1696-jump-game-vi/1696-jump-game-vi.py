class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        Q = collections.deque([])
        Dp = [0]*len(nums)

        for i in range(len(nums)):
            #when i - Q[0] > k, we throw the index away.
            while(len(Q) > 0 and i - Q[0] > k):
                Q.popleft()

            if len(Q) == 0:
                Dp[i] = nums[i]
                Q.append(i)
            else:
                Dp[i] = nums[i] + Dp[Q[0]]
                #The reason that we abandon the rightmost ele (Q[-1]) if Dp[Q[-1]] <= Dp[i], is that we only #cares about the element that can give us LARGER Dp
                while(len(Q) > 0 and Dp[Q[-1]] <= Dp[i]):
                    Q.pop()    
                Q.append(i)

        return Dp[-1]

