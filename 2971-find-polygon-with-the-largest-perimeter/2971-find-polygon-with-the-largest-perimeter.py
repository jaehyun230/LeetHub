class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        answer = -1
        n = len(nums)
        
        if n < 3 :
            return answer
        
        nums.sort()
        
        dp = [0] * n
        dp[0], dp[1] = nums[0], nums[1]+nums[0]
        
        for i in range(2, n) :
            dp[i] = dp[i-1] + nums[i]
            if nums[i] < dp[i-1] :
                answer = max(answer, dp[i])
        
        
        return answer