class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        s=set(arr)
        for i in range(1,10000):
            if i not in s:
                if k==1:
                    return i
                k-=1