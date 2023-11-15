class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        min_prod = 1
        stack = []
        for i in range(len(nums)) :
            
            i_sum = 0 #the subarray sum over which i is minimum
            while stack and stack[-1][0] >= nums[i]:
                j, j_sum = stack.pop()
                min_prod = max(min_prod, j*(i_sum + j_sum))
                i_sum += j_sum #subarray sum gets transferred to new smaller element
            
            stack.append([nums[i], i_sum + nums[i]])
        
        c_sum = 0
        while stack:
            j, j_sum = stack.pop()
            c_sum += j_sum
            min_prod = max(min_prod, j*c_sum)
        
            
        return min_prod%(10**9 + 7)