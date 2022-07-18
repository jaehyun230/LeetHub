from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        answer = 0
        
        n, m = len(matrix), len(matrix[0])
        
        dp = defaultdict(int)
        
        for i in range (n) :
            for j in range (m) :
                dp[i, j] = dp[i-1, j] + dp[i, j-1] - dp[i-1, j-1] + matrix[i][j]
        
        
        for x in range (n) :
            for x2 in range (-1, x) :
                counts = defaultdict(int)
                
                for k in range (-1, m) :
                    c_psum = dp[x, k] - dp[x2, k]
                    answer += counts[c_psum - target]
                    counts[c_psum] += 1
                    
        return answer 