class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        #결과 값들
        answer = []
        #현재 even_sum 값
        even_sum = 0
        
        for num in nums :
            if num%2 == 0 :
                even_sum += num
                
        for val, index in queries :
            if nums[index] %2 == 0 and val %2 == 0 :
                even_sum += val
            elif nums[index] %2 == 0 and val %2 != 0 :
                even_sum -=nums[index]
            elif nums[index] %2 != 0 and val %2 != 0 :
                even_sum += nums[index] + val
            
            nums[index] +=val
            answer.append(even_sum)
        
        return answer