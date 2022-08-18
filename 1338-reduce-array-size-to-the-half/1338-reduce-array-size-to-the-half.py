class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for x in arr:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
                  
        l = sorted(d.values())
            
        N = len(arr) // 2
        idx = 0
        
        while N > 0:
            N -= l[-idx-1]
            idx += 1
            
        return idx