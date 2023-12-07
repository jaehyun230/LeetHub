class Solution:
    def largestOddNumber(self, num: str) -> str:
        temp = list(num)
        for i in range(len(temp)-1, -1, -1) :
            if int(temp[i]) %2 == 1 :
                return "".join(temp[:i+1])
        
        return ""
        