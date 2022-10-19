import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dic = {}
        
        for word in words :
            if word not in dic :
                dic[word] = 1
            else :
                dic[word] +=1
        
        heap = []
        
        for i in dic :
            heapq.heappush(heap, [-dic[i], i])
        
        answer = []
        
        while k > 0 :
            num, target = heapq.heappop(heap)
            answer.append(target)
            k -=1
        
        return answer