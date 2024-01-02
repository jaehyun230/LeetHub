class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        dic = {}
        for num in nums :
            if num not in dic :
                dic[num] = 1
            else :
                dic[num] +=1
        
        
        result = []
        check = True
        while check :
            temp = []
            check = False
            for key in dic :
                if dic[key] > 0 :
                    temp.append(key)
                    dic[key] -=1
                    check = True
            
            if temp :
                result.append(temp)
                
        return result