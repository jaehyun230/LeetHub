class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        dic = {}
        
        answer = 0
        
        for i in s :
            if i not in dic :
                dic[i] = 1
            else :
                dic[i] +=1
        
        for j in t :
            if j in dic :
                if dic[j] != 0 :
                    dic[j]-=1
                else :
                    answer +=1
            else :
                answer +=1
        
        return answer