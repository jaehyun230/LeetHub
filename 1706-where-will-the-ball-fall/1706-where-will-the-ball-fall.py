class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[i for i in range(COLS)] for _ in range(ROWS + 1)]
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS):
                nc = c + grid[r][c]
                if nc < 0 or nc == COLS or grid[r][nc] != grid[r][c]:
                    dp[r][c] = -1
                else:
                    dp[r][c] = dp[r + 1][nc]
        
        return dp[0]