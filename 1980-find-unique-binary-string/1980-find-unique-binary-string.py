class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        answer = ""
        
        for i in range(len(nums)):
            if nums[i][i]=="0":
                answer=answer+"1"
            else:
                answer=answer+"0"
        
        return answer
        