class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        temp = ""
        
        for i in digits :
            temp +=str(i)
        
        value = int(temp)+1
        
        arr = str(value)
        
        answer = []
        
        for i in arr :
            answer.append(int(i))
        
        return answer