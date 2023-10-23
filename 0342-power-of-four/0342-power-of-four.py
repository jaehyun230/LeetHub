class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        while n >= 4 :
            if n%4 == 0 :
                n = n//4
            else :
                return False
        
        if n == 1 :
            return True