class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums.sort()
        res = [[num] for num in nums]  #contains sets starting with that number
        
        for i in range(n):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and len(res[i]) < len(res[j]) + 1:  
                    res[i] = res[j] + [nums[i]]
                    
        return max(res, key=len)  #return max length set