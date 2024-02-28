class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        sign = True
        start = True
        num = 0
        if len(s) == 0 :
            return 0
        if s[0] == '-' :
            sign = False
        for c in s :
            print(c)
            if c.isdigit() :
                num = num*10 + int(c)
            elif c == '-' or c =='+' :
                if start == True :
                    start = False
                    continue
                else :
                    break
            else :
                break
            
            if start == True :
                start = False
        
        if sign == False :
            num *=-1
        
        if -2**31 <= num <= 2**31-1 :
            return num
        elif sign :
            return 2**31 -1
        
        return -2**31