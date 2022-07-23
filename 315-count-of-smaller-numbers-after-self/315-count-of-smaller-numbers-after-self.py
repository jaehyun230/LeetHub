import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        answer =sorted(nums)
        
        
        result=[]
        
        for i in nums:
            index = bisect.bisect_left(answer,i)
            result.append(index)
            del answer[index]
            
        return result