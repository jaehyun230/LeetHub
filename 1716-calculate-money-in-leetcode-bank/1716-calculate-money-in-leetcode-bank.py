class Solution:
    def totalMoney(self, n: int) -> int:
        
        answer = 0
        for i in range(n) :
            temp = i//7+1 + i%7
            answer +=temp
        
        return answer