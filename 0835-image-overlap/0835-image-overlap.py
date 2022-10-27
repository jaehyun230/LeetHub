class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        m = len(img1)
        n = len(img1[0])
        
        la = []
        lb = []
        
        v = collections.Counter()
        
        for r in range(m):
            for c in range(n):
                if img1[r][c] == 1:
                    la.append((r, c))
                if img2[r][c] == 1:
                    lb.append((r, c))
        
        for ax, ay in la:
            for bx, by in lb:
                k = (ax-bx, ay-by)
                v[k] += 1
        
        return max(v.values() or [0])