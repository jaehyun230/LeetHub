class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k<=1: return 0
        
        log_k = math.log(k)
        count = 0
        summ = 0
        
        left = 0
        for right, num in enumerate(nums):
            summ += math.log(num)
            while summ > log_k or math.isclose(summ, log_k): # compare floats 
                summ -= math.log(nums[left])
                left += 1
            count += right-left+1
            
        return count