from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def bfs(a, b) :
            q = deque()
            q.append((a, b))
            grid[a][b] = 1
            while q :
                x, y = q.popleft()
                for k in range(4) :
                    mx = x+dx[k]
                    my = y+dy[k]
                    
                    if 0 <= mx < len(grid) and 0 <= my < len(grid[0]) and grid[mx][my] == "1" :
                        grid[mx][my] = "0"
                        q.append((mx, my))
        
        for i in range (len(grid)) :
            for j in range(len(grid[i])) :
                if grid[i][j] == "1" :
                    bfs(i,j)
                    answer +=1
        
        return answer
                
        
        
            