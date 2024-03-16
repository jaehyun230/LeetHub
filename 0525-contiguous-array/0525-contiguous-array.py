class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        dic = {}
        dic[0] = -1
        prefixsum = 0
        
        answer = 0
        
        for idx, num in enumerate(nums) :
            if num == 1 :
                prefixsum +=1
            else :
                prefixsum -=1
            
            if prefixsum in dic :
                answer = max(answer, idx - dic[prefixsum])
            else :
                dic[prefixsum] = idx
        
        return answer