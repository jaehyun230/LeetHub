class Solution:
    def reverse(self, x: int) -> int:
        
        x=str(x)
        if x[0] != '-' :
            x = x[::-1]
        else :
            x = x[1:]
            x = '-' + x[::-1]
        
        if abs(int(x)) > 2**31 -1 :
            return 0
        
        return int(x)