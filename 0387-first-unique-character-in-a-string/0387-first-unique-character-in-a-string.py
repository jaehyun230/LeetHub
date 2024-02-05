class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dic = {}
        
        for index, c in enumerate(s) :
            if c not in dic :
                dic[c] = index
            else :
                dic[c] = -1
                
        for k in dic :
            if dic[k] >= 0 :
                return dic[k]
        
        return -1