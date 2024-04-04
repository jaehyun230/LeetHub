class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        
        answer = 0
        for i in s :
            if i == "(" :
                stack.append("(")
                answer = max(answer, len(stack))
            elif i == ")" :
                stack.pop()
        
        return answer