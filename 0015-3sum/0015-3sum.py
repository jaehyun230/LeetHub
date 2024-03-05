class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = set()
        
        nums.sort()
        n = len(nums)
        
        for i in range(n-2) :
            
            left = i+1
            right = n-1
            
            if left == right :
                continue
            
            while left < right :
                target =  nums[i] + nums[left] + nums[right]
                if target == 0 :
                    answer.add((nums[i], nums[left], nums[right]))
                    left +=1
                elif target < 0 :
                    left +=1
                elif target > 0 :
                    right -=1
             
        return list(answer)