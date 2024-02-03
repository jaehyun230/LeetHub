class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        ans = -float('inf')
        prefix = [0]
    
        dic = {}
  
        for i, num in enumerate(nums):
            prefix.append(prefix[-1] + num)
	  
            if (num - k) in dic:
                ans = max(ans, prefix[i + 1] - prefix[dic[num - k] + 1] + nums[dic[num - k]])
            if (num + k) in dic:
                ans = max(ans, prefix[i + 1] - prefix[dic[num + k] + 1] + nums[dic[num + k]])
      
            if num in dic:
                if (prefix[i + 1] - prefix[dic[num] + 1] + nums[dic[num]] >= num):
                    continue
            dic[num] = i
        
        return int(ans) if ans != -float('inf') else 0