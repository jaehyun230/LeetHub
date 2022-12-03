class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        c=sorted(c.items(), key=lambda kv : (kv[1],kv[0]), reverse = True)
        t,n='',len(c)
        for i in range(n):
            t+=c[i][0]*c[i][1]
        return t