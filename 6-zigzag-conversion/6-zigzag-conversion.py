from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 :
            return s
        
        answer = ""
        
        dic = defaultdict(list)
        
        reverse = True
        count = 1
        
        for i in range(len(s)) :
            dic[count].append(s[i])
            if count == 1 :
                reverse = False
            if count == numRows :
                reverse = True
            
            if reverse == False :
                count +=1
            else :
                count -=1
                  
        for i in range (1, numRows+1) :
            while dic[i] :
                answer += dic[i].pop(0)
                       
        return answer