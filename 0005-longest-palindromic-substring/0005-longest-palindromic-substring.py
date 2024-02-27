class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        def bfs(left, right) :
                
            while left>= 0 and right < len(s) and s[left] == s[right] :
                left -=1
                right +=1
            
            return s[left+1 :right]
            
        for i in range(len(s)) :
            answer = max(bfs(i, i), bfs(i, i+1), answer, key = len)
        
        return answer