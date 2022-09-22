class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        
        words = s.split()
        
        for word in words :
            word = word[::-1]
            answer += word + ' '
        
        answer = answer[:-1]
        
        return answer