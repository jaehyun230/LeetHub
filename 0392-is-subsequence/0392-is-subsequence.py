class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        point = 0
        answer = False
        if len(s) == 0 :
            return True
        for i in s :
            if point == len(t) :
                return False
            if len(t) == 0 :
                return False
            for k in range(point, len(t)) :
                if i == t[k] :
                    point = k+1
                    break
                if k == len(t)-1 :
                    return False
        
        return True