class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for c in s :
            if stack and stack[-1].isupper() and stack[-1].lower() == c:
                stack.pop()
            elif stack and stack[-1].islower() and stack[-1].upper() == c:
                stack.pop()
            else :
                stack.append(c)
        
        return "".join(stack)