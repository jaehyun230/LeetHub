class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d1 = {}
        d2 = {}
        cnt = 0
        for i in range(len(s)):
            if s[i] not in d1:
                if t[i] in d2: return False
                d1[s[i]] = cnt
                d2[t[i]] = cnt
                cnt += 1
            elif t[i] not in d2: return False
            elif d1[s[i]] != d2[t[i]]: return False
            
        return True