class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for i in range (len(nums)) :
            if nums[i] not in dic :
                dic[nums[i]] = i
            if target-nums[i] in dic :
                if dic[target-nums[i]] != i :
                    return[dic[target-nums[i]], i]