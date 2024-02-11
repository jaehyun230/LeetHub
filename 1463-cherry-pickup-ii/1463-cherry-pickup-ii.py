class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        if grid == [[]]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
      
        def dfs(row, c1, c2,seen):
            
            if c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
                return - float("inf")
            
            if((row,c1,c2) in seen):
                return seen[(row,c1,c2)]
            
            res = 0
            res += grid[row][c1] + grid[row][c2]
            
            if c1 == c2: 
                res -= grid[row][c1]
                
            if row < m - 1: 
                res += max(dfs(row + 1, i, j, seen)
                          for i in [c1 - 1, c1, c1 + 1]
                          for j in [c2 - 1, c2, c2 + 1])
                
            seen[(row,c1,c2)] = res
            
            return seen[(row,c1,c2)]
        
        
        seen = {}
        return dfs(0, 0, n - 1,seen)
            
                
            