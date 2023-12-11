class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        dic = {}
        
        for i in arr :
            if i not in dic :
                dic[i] = 1
            else :
                dic[i] +=1
        
        for k in dic :
            if dic[k] > len(arr)/4 :
                return k