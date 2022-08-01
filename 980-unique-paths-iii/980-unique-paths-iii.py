class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        need = 1
        global answer
        answer = 0
        
        def dfs(x, y, path) :
            
            global answer
            for i in range(4) :
                mx = x+dx[i]
                my = y+dy[i]
                
                if 0 <= mx < len(grid) and 0 <= my < len(grid[0]) and [mx, my] not in path :
                    
                    if grid[mx][my] == -1 :
                        continue
                    elif grid[mx][my] == 2 :
                        if len(path) == need :
                            answer +=1
                    else :
                        dfs(mx, my, path + [[mx, my]])
            
            
        
        for i in range (len(grid)) :
            for j in range (len(grid[i])) :
                if grid[i][j] == 0 :
                    need +=1
        
        for i in range (len(grid)) :
            for j in range (len(grid[0])) :
                if grid[i][j] == 1 :
                    dfs(i, j, [[i, j]])
                    return answer
                    
        
        
            
            