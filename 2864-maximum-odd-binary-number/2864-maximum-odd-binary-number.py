class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = s.count("1") - 1
        len_s = len(s)
        
        answer = ""
        for i in range(n) :
            answer +="1"
        for j in range(len_s-n-1) :
            answer +="0"
        
        answer +="1"
        
        return answer