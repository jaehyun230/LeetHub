class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        def posToval(r, c):
            return r * n + c
        def valTopos(v) :
            return [v// n, v % n]
        
        graph = [[0] * n for i in range(m)]
        for i in range(m) :
            for j in range(n) :
                new_val = (posToval(i, j)+k) % (m * n)
                new_r, new_c = valTopos(new_val)
                graph[new_r][new_c] = grid[i][j]
                
        return graph