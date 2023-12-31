class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        answer = -1
        data = list(s)
        for i in range(len(s)-1) :
            for j in range(i+1, len(s)) :
                
                if data[i] == data[j] :
                    answer = max(answer, j-i-1)
        
        return answer