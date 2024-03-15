class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        count = 0
        alls = 1
        for num in nums :
            if num == 0 :
                count +=1
            else :
                alls *=num
        
        answer = []
        
        for num in nums :
            if count >= 2 :
                answer.append(0)
            elif count == 1 and num != 0 :
                answer.append(0)
            elif count == 1 and num == 0 :
                answer.append(alls)
            else :
                answer.append(alls//num)
        
        return answer