class Solution:
    def pivotInteger(self, n: int) -> int:
        
        answer = -1
        
        total = sum(range(n+1))
        pre_sum = 0
        
        for i in range(n, -1, -1) :
            pre_sum +=i
            if pre_sum == total :
                return i
            total -=i
        
        return answer