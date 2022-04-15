class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        cursor = 0
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV" : 4, "IX" : 9
              , "XL": 40, "XC": 90, "CD" : 400, "CM" : 900}
        
        while cursor < len(s) :
            
            if cursor+1 < len(s) and (s[cursor]+s[cursor+1]) in dic :
                sum += dic[(s[cursor]+s[cursor+1])]
                cursor +=2
            
            else :
                sum += dic[s[cursor]]
                cursor +=1
        return sum
        