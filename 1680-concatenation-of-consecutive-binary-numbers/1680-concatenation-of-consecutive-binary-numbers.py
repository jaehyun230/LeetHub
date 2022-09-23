class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # modulo 10^9 + 7
        
        answer = ""
        for i in range(1, n+1) :
            answer += bin(i)[2:]
        
        answer = int(answer, 2)%(10**9+7)
        
        return answer