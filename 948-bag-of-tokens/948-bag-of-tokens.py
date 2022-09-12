class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        answer = 0
        now = 0
        
        arr = sorted(tokens)
        
        left = 0
        right = len(tokens)-1
        
        while left <= right :
           
            if power >= arr[left] :
                power -=arr[left]
                left +=1
                now +=1   
            else :
                if now <= 0 :
                    break
                power +=arr[right]
                right -=1
                now -=1
                
            answer = max(answer, now)
        
        
        return answer
        