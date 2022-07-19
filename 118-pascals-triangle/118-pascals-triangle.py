class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        
        for i in range (numRows-1) :
            temp = []
            for j in range(len(answer[i])) :
                if j == 0 :
                    temp.append(1)
                
                else :
                    value = answer[i][j-1] + answer[i][j]
                    temp.append(value)
                    
                if j == len(answer[i]) - 1 :
                    temp.append(1)
                
            answer.append(temp)
        
        
        return answer
        