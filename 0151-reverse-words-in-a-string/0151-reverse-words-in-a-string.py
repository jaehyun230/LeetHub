class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s.split())
        words = words[::-1]
        
        answer = ""
        for word in words :
            answer+= word
            answer+= " "
        
        return answer[0:-1]