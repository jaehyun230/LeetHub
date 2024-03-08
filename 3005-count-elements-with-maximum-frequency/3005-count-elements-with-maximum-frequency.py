class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        answer = 0
        dic = {}
        
        for num in nums :
            if num not in dic :
                dic[num] = 1
            else :
                dic[num] +=1
                
        max_value = max(dic.values())
        for i in dic :
            if dic[i] == max_value :
                answer += max_value
        
        return answer