from collections import defaultdict

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        answer = [[0]*len(grid[0]) for i in range(len(grid))]
        
        dic_col = defaultdict(int)
        dic_row = defaultdict(int)
        
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                value = 1
                if grid[i][j] == 0 :
                    value = -1
                    
                if i not in dic_col :
                    dic_col[i] = value
                else :
                    dic_col[i] += value
                    
                if j not in dic_row :
                    dic_row[j] = value
                else :
                    dic_row[j] +=value
        
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                answer[i][j] = dic_col[i] + dic_row[j]
                
                
        
        
        
        return answer
    