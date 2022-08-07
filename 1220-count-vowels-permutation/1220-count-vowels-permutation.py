class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        choice = {"a":["e"], "e":["a", "i"], "i":["a", "e", "o", "u"], "o":["i", "u"], "u":["a"]}
        dp = {}
        
        def solve(i, c):
            if(i == n):
                return 1
            key = (i, c[-1])
            if(key in dp):
                return dp[key]
            t = 0
            for j in choice[c[-1]]:
                t += solve(i + 1, c + j)
            dp[key] = t 
            return t
        
        ans = 0
        for i in choice.keys():
            ans += solve(1, i)
        return ans % 1000000007