class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s :
            if i == "(" :
                stack.append(i)
            elif i == ")" :
                if stack and stack[-1] == "(" :
                    stack.pop()
                else :
                    return False
            
            if i == "{" :
                stack.append(i)
            elif i == "}" :
                if stack and stack[-1] == "{" :
                    stack.pop()
                else :
                    return False
                
            if i == "[" :
                stack.append(i)
            elif i == "]" :
                if stack and stack[-1] == "[" :
                    stack.pop()
                else :
                    return False
        
        if len(stack) == 0 :
            return True
        else :
            return False