class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        
        m = min([len(s) for s in strs])
        
        for i in range (m) :
            check = strs[0][i]
            flag = True
            for j in range(len(strs)) :
                if check != strs[j][i] :
                    flag = False
                    break
            
            if flag :
                answer +=check
            else :
                break
        
        return answer