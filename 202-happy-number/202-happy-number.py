class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1 :
            return True
        
        total = 0
        while n>0 :
            total += pow(n%10, 2)
            n  //= 10
            
        if total == 2 or total == 4 or total == 6 or total == 8 :
            return False
        
        return Solution().isHappy(total)
            