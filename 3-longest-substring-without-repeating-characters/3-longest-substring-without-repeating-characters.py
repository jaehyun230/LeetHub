from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        que = deque()
        
        answer = 0
        
        for i in s :
            if i in que :
                while que :
                    que.popleft()
                    if i not in que :
                        break
            que.append(i)
            
            answer = max(answer, len(que))
        
        
        return answer