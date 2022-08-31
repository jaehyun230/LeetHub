from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
            
        m, n = len(heights), len(heights[0])
        
        def bfs(que):
            visited = set()
            while que:
                x,y = que.popleft()
                if (x,y) in visited : 
                    continue
                visited.add((x,y))
                for i in range(4) :
                    mx = x+dx[i]
                    my = y+dy[i]
                    if 0 <= mx < m and 0 <= my < n:
                        if heights[x][y] <= heights[mx][my]:
                            que.append((mx, my))
            return visited
        
        #Pacific
        que1 = deque()
        for i in range(m):
            que1.append((i, 0))
        for j in range(n):
            que1.append((0, j))
            
        #Atlantic
        que2 = deque()
        for i in range(m):
            que2.append((i,n-1))
        for j in range(n):
            que2.append((m-1,j))
            
        return list(bfs(que1) & bfs(que2))
        
            