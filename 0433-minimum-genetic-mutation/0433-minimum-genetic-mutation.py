from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def differ_dist(arr1, arr2) :
            
            differ = 0
            for i in range(len(arr1)) :
                if arr1[i] != arr2[i] :
                    differ +=1
            return differ
         
        q = deque()
        q.append((start,0))
        
        mutations = set()
        mutations.add(start)
        while q:
            now, dist = q.popleft()
            if now == end:
                return dist
            
            for mutation in bank:
                if differ_dist(now,mutation) == 1 and mutation not in mutations:
                    mutations.add(mutation)
                    q.append((mutation,dist+1))
            

        return -1