class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        n = len(pref)
        answer = [0] * n
        answer[0] = pref[0]
        
        for i in range (1, n) :
            answer[i] = pref[i]^pref[i-1]
        
        return answer
            
        
        