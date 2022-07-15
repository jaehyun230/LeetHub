from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def bfs(a, b) :
            q = deque()
            q.append((a, b))      
            count = 0
            visited[a][b] = 1
            
            while q :
                x, y = q.popleft()
                count +=1
                for i in range (4) :
                    mx = x+dx[i]
                    my = y+dy[i]
                    
                    if 0 <= mx < len(grid) and 0 <= my < len(grid[0]) and grid[mx][my] == 1 and visited[mx][my] == 0 :
                        visited[mx][my] = 1
                        q.append((mx, my))
                         
            return count
                                
        answer = 0
              
        visited = [[0] * len(grid[0]) for _ in range (len(grid))]
        
        for i in range (len(grid)) :
            for j in range (len(grid[0])) :
                if grid[i][j] == 1 and visited[i][j] == 0 :
                    val = (bfs(i, j))
                    answer = max(answer , val)
                    
        return answer
                