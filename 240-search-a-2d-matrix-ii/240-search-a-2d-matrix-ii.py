class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        bottom = 0
        top = len(matrix) -1
        
        while bottom <= top :
            left = 0
            right = len(matrix[0])-1
                     
            while left <= right :
                
                mid = (left+right)//2
                
                if matrix[bottom][mid] == target :
                    return True
                
                elif matrix[bottom][mid] > target :
                    right = mid - 1
                    
                else :
                    left = mid + 1
            
            
            bottom +=1
            
        
        return False
        