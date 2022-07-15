class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()    
        answer = None
        diff = float('inf')
                       
        for i in range(len(nums)-2) :           
            start = i +1
            end = len(nums) -1
            
            while start < end :
                sum_value = nums[i] + nums[start] + nums[end]
                
                     
                if sum_value == target :
                    return target
                
                else :
                    curr_diff = abs(sum_value - target)  
                    
                    if curr_diff < diff :
                        diff = curr_diff
                        answer = sum_value   
                        
                    if sum_value < target:
                        start +=1
                    else :
                        end -=1
        
        return answer