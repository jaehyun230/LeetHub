class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        count, vowels = 0, 'a,e,i,o,u,A,E,I,O,U'
        
        for i in range(len(s)//2):
            count += s[i] in vowels
            count -= s[~i] in vowels
        
        return not count