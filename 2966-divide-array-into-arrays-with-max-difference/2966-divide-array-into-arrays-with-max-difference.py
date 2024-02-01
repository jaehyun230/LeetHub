class Solution:
    
    
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        answer = []
        n = len(nums)
        
        if n == 1 :
            return []
        
        nums.sort()
        divide = n//3
        
        for i in range(divide) :
            if nums[i*3+2] - nums[i*3] <= k :
                answer.append([nums[i*3], nums[i*3+1], nums[i*3+2]])
            else :
                return []
        
        return answer
        