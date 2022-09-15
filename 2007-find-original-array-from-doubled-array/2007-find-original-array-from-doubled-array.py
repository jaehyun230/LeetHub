class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed)%2 != 0 :
            return []
        
        changed.sort()
        
        answer = []
        
        dic = {}
        
        for val in changed :
            if val/2 in dic :
                dic[val/2] -=1
                if dic[val/2] == 0 :
                    del dic[val/2]
                answer.append(int(val/2))
            else :
                if val not in dic :
                    dic[val] = 1
                else :
                    dic[val] +=1
                
        if len(answer) == len(changed)/2 :
            return answer
        
        return []
        