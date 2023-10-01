class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        temp = ""
        for i in s :
            if i !=" " :
                temp = i + temp
            else :
                answer +=temp
                answer +=i
                temp = ""
        
        if temp !="" :
            answer +=temp
        
        return answer
        