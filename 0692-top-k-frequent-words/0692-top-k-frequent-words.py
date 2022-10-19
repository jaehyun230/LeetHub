class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dic = {}
        
        for word in words :
            if word not in dic :
                dic[word] = 1
            else :
                dic[word] +=1
        
        dic = dict(sorted(dic.items()))
        
        sorted_dict = dict(sorted(dic.items(), key = lambda item: item[1], reverse = True))
        
        answer = []
        
        count = 0
        for i in sorted_dict :
            if count == k :
                break
            answer.append(i)
            count +=1
            
        return answer