class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        dic = {}
        
        answer = 0
        
        for num in nums :
            if num not in dic :
                dic[num] = 1
            else :
                dic[num] +=1
        
        for key in dic :
            
            if dic[key] == 1 :
                return -1
            elif dic[key]%3 == 1 :
                answer += dic[key]//3 + 1
            elif dic[key]%3 == 2 :
                answer += dic[key]//3 + 1
            elif dic[key]%3 == 0 :
                answer += dic[key]//3
            
            elif dic[key]%2 == 0 :
                answer += dic[key]//2
        
        
        return answer