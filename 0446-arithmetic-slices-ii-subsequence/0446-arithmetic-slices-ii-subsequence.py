class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i, d] = number of arithmatic subsequences of length at-least 2 with common
        #            difference "d" and subsequence ends on i
        dp = Counter()

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i, d] += dp[j, d] + 1  # +1 for counting subsequence (A[j], A[i])

        return dp.total() - comb(n, 2)  # removing subsequences of size 2