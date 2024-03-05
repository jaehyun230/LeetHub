class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        n = len(nums)
        for i in range(n) :
            dic[nums[i]] = i
        
        for i in range(n) :
            if target - nums[i] in dic and i != dic[target - nums[i]] :
                
                return [i, dic[target-nums[i]]]