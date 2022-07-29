class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []
        
        
        
        for word in words :
            
            if len(set(word)) != len(set(pattern)) :
                continue
            
            dic = {}
        
            for i in range(len(word)) :
                if word[i] not in dic :
                    dic[word[i]] = pattern[i]
                
                else :
                    if dic[word[i]] != pattern[i] :
                        break
                
                if i == len(word) - 1 :
                    answer.append(word)
        
        return answer