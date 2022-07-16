from collections import deque

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        memo = {}
        mod = 1000000007

        def solve(x: int, y: int, move: int) -> int:
            if move > maxMove:
                return 0
            if x not in range(m) or y not in range(n):
                return 1
            if (x, y, move) in memo:
                return memo[(x, y, move)] % mod
            memo[(x, y, move)] = solve(x, y - 1, move + 1) + solve(x - 1, y, move + 1) + \
                                 solve(x, y + 1, move + 1) + solve(x + 1, y, move + 1)
            return memo[(x, y, move)] % mod

        return solve(startRow, startColumn, 0) % mod