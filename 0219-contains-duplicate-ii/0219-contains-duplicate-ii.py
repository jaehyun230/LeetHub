from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dic = defaultdict(int)
        
        if k == 0 :
            return False
        
        for i in range(len(nums)) :
            
            if i <= k :
                if nums[i] in dic :
                    
                    return True
                dic[nums[i]] +=1
            else :
                dic[nums[i-k-1]] -=1
                if dic[nums[i]] > 0 :
                    return True
                dic[nums[i]] +=1
            
    
        return False