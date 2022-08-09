from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        #중복제거
        dic = defaultdict(set)   
        arr.sort()
        
        for i in range (len(arr)) :
            for j in range (i) :
                if arr[i] % arr[j] == 0 :
                    res = arr[i]//arr[j]
                    if res in arr :
                        dic[i].add((j, arr.index(res)))
        @cache
        def dfs(i):
            now = 1
            for l, r in dic[i]: 
                now += dfs(l) * dfs(r)
            return now
        
        ans = 0           
        for i in range(len(arr)):        
            ans += dfs(i)        
        return ans %(10**9 + 7)
        
            