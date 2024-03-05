class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []
        
        def backtrack(now, a, b) :
            if a == 0 and b == 0 :
                answer.append(now)
                return
            if a > 0 :
                backtrack(now+"(", a-1, b)
            if a < b :
                backtrack(now+")", a, b-1)
                
            
        backtrack("", n, n)
        
        
        return answer