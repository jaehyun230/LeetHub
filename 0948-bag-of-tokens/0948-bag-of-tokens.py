class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        
        tokens.sort()
        left, right = 0, len(tokens) - 1
        point = 0
        answer = 0
        
        while left <= right :
            if power >= tokens[left] :
                power -=tokens[left]
                left +=1
                point +=1
                
            else :
                if point <= 0 :
                    break
                power += tokens[right]
                point -=1
                right -=1
            
            answer = max(answer, point)
            
            
        return answer