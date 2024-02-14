class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = []
        neg = []
        
        for num in nums :
            if num >= 0 :
                pos.append(num)
            else :
                neg.append(num)
        
        answer = []
        n = len(nums)//2
        
        for i in range(n) :
            answer.append(pos[i])
            answer.append(neg[i])
        
        return answer