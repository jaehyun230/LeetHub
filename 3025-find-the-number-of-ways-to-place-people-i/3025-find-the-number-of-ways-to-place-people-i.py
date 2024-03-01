class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        answer = 0
        n = len(points)
        for i in range(n) :
            for j in range(n) :
                if i == j :
                    continue 
                if points[i][0] >= points[j][0] and points[i][1] <= points[j][1] :
                    for k in range(n) :
                        if k != i and k!= j :
                            if points[i][0] >= points[k][0] and points[j][0] <= points[k][0] and points[i][1] <= points[k][1] and points[j][1] >= points[k][1] :
                                break
                        if k == n-1 :
                            answer +=1

        return answer



print(Solution().numberOfPairs([[2,6],[4,4],[6,2]]))