class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        answer = s[0]
        for i in range(len(s)) :
            for j in range(i, len(s)) :
                arr = s[i:j+1]
                if len(arr) > len(answer) and arr == arr[::-1] :
                    answer = arr
        
        return answer