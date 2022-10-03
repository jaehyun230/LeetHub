class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = []
        
        answer = 0
        
        for i, color in enumerate(colors) :
            if len(stack) == 0 :
                stack.append((color, neededTime[i]))
            else :
                if stack[-1][0] == color :
                    if stack[-1][1] < neededTime[i] :
                        answer +=stack[-1][1]
                        stack.pop()
                        stack.append((color, neededTime[i]))
                    else :
                        answer +=neededTime[i]
                else :
                    stack.append((color, neededTime[i]))
                    
            
        
        return answer