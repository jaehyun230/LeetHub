class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        dic = {}
        now = 0
        
        for i, val in enumerate(nums) :
            now +=val
            remain = now%k
            
            if remain == 0 and i >= 1 :
                return True
            
            if remain in dic :
                if i - dic[remain] >= 2 :
                    return True
            
            #dic.get -> remain key none than i get
            dic[remain] = min(dic.get(remain, i), i)
        
        return False
        
        