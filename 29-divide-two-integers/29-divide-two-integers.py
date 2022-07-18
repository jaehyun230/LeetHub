class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        limit = pow(2,31) - 1
        
        if dividend * divisor > 0 :
            
            answer = dividend // divisor
        
        else :
            
            if dividend % divisor == 0 :
                answer = dividend // divisor
            else :
                answer = dividend // divisor + 1
        
        if answer > limit :
            answer = limit
        
        return answer