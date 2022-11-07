class Solution:
    def maximum69Number (self, num: int) -> int:
        numbers = str(num)
        result = ''
        find = False
        for i, val in enumerate(numbers) :
            if val == '6' and find == False :
                find = True
                result +='9'
            else :
                result +=val
        
        result = int(result)
        
        return result
                