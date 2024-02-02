class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        answer = []
        for i in range(1, 10) :
            temp = i
            for j in range(i+1, 10) :
                temp = temp*10 + j
                if low <= temp <= high :
                    answer.append(temp)
        answer.sort()
        return answer
                
        
        
        