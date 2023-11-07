class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        dic = defaultdict(int)
        nums.sort()
        
        answer = []
        for k in range(0, len(nums)) :
            dic[nums[k]] = k
        
        for i in range(0, len(nums)-1) :
            for j in range(i+1, len(nums)) :
                
                target = (nums[i] + nums[j])*-1
                if target in dic :
                    if dic[target] > j :
                        if [nums[i], nums[j], target] not in answer :
                            answer.append([nums[i], nums[j], target])
        
       
        
        return answer