class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        
        answer = 1
        
        for i in range(1, len(arr)) :
            if arr[i] - arr[i-1] >= 1 or arr[i] > i :
                answer +=1
        
        
        return answer