class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        dic = defaultdict(list)
        
        for i in range (len(nums)-1, -1, -1) :
            for j in range(len(nums[i])) :
                dic[i+j].append(nums[i][j])
        
        max_val = max(dic)
        answer = []
        for i in range(max_val+1) :
            for k in dic[i] :
                answer.append(k)
        
        return answer