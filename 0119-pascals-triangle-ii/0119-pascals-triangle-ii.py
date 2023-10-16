class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        row = [1]
        
        for i in range (1, rowIndex+1) :
            temp = [0] * (i+1)
            temp[0], temp[-1] = 1, 1
            for j in range (1, i) :
                temp[j] = row[j-1] + row[j]
            
            row = temp
        
        return row
            
            
            