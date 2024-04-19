from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.answer = 0
        
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        q = deque()        
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if visited[i][j] == False and grid[i][j] == "1" :
                    q.append([i, j])
                    while q :
                        x, y = q.popleft()
                        
                        for k in range(4) :
                            mx = x + dx[k]
                            my = y + dy[k]
                            
                            if 0 <= mx < len(grid) and 0 <= my < len(grid[0]) and visited[mx][my] == False :
                                if grid[mx][my] == "1" :
                                    visited[mx][my] = True
                                    q.append([mx, my])
                    
                    self.answer +=1
                                
        
        return self.answer