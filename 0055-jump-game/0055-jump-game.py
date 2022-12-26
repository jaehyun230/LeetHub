class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        now = 0
        
        for i, n in enumerate(nums):
            if i > now:
                return False
            now = max(now, i+n)
        return True