class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        answer = ""
        reset = False
        for i in s :
            if i == " " :
                reset = True
            else :
                if reset == True :
                    answer = ""
                    reset = False
                answer +=i
        
        return len(answer)