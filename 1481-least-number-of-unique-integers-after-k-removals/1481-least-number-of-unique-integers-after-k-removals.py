class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        dic = {}
        
        for n in arr :
            if n not in dic :
                dic[n] = 1
            else :
                dic[n] +=1
        
        sorted_dic = sorted(dic.items(), key = lambda item: item[1])
        
        answer = len(sorted_dic)
        for _, count in sorted_dic :
            if k >= count :
                k -=count
                answer -=1
            else :
                break
        
        return answer