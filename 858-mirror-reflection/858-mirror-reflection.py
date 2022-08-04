class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        gcd = math.gcd(p, q)
        
        p //= gcd
        q //= gcd
        
        if p%2==0 and q%2==1:
            return 2
        
        elif p%2==1 and q%2==0: 
            return 0
        
        else: 
            return 1