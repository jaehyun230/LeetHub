class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0 :
            return False
        while n > 1 :
            if n%2 == 0 :
                n = n//2
            elif n%2 != 0 :
                return False
        
        return True