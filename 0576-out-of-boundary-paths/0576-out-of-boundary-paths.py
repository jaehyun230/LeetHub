class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def dp(x, y, remainingMoves):
            if (x, y, remainingMoves) in memo:
                return memo[(x, y, remainingMoves)]

            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            if remainingMoves == 0:
                return 0

            paths = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                paths += dp(x + dx, y + dy, remainingMoves - 1)
                paths %= MOD

            memo[(x, y, remainingMoves)] = paths
            return paths

        return dp(startRow, startColumn, maxMove)