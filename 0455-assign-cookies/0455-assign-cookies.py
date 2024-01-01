class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        response = 0
        while g and s:
            if s[-1] >= g[-1]:
                s.pop()
                g.pop()
                response += 1
            else:
                g.pop()
        return response