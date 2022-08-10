import heapq

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        start = len(nums)-1
        
        for i in range(len(nums) - 1, -1, -1):
            if start <= i + nums[i]:
                start = i
            
            
        if start == 0 :
            return True
        else :
            return False