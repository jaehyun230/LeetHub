class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
           
        start = 0
        end = len(nums)-1     
        find = False
        
        while start <= end :
            mid = (start+end)//2
            
            if nums[mid] == target :
                find = True
                
                for start_index in range(mid,-1,-1):
                    if nums[start_index] == target :
                        start = start_index
                    else :
                        break
                for end_index in range(mid, len(nums)) :
                    if nums[end_index] == target :
                        end = end_index
                    else :
                        break
                break
                
            elif nums[mid] > target :
                end = mid - 1
            else :
                start = mid + 1
        
        if find :
            return [start, end]
        else :
            return [-1, -1]
        
        