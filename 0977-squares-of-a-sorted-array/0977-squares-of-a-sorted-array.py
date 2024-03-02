class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        answer = [0] * len(nums)
        
        left, right = 0, len(nums)-1
        
        while left <= right :
            left_val = nums[left]**2
            right_val = nums[right]**2
            
            if left_val <= right_val :
                answer[right-left] = right_val
                right -=1
            else :
                answer[right-left] = left_val
                left +=1
            
        return answer