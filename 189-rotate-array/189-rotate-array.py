class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n =  k % len(nums)     
        nums.reverse()
        
        for i in range(n) :
            if n-1-i < i or i == n - 1 - i :
                break
            nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
        
        
        for i in range(n, len(nums)) :
            if len(nums) -1 -(i-n) < i or i == len(nums) -1 -(i-n) :
                break
            
            nums[i], nums[len(nums) -1 -(i-n)] = nums[len(nums) -1 -(i-n)], nums[i]