class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        
        for i in range (len(s)) :
            if s[i] in dic :
                dic[s[i]] = len(s)
            else : 
                dic[s[i]] = i
                
        for i in dic :
            if dic[i] < len(s) :
                return dic[i]
        
        return -1