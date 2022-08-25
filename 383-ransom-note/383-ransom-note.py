from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dic = defaultdict(int)
        for i in magazine :
            dic[i] +=1
        
        for j in ransomNote :
            dic[j] -=1
            if dic[j] < 0 :
                return False
        
        return True