import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q = []
        
        for i in range(len(matrix)) :
            for j in range(len(matrix)) :
                heapq.heappush(q, matrix[i][j])
        
        answer = matrix[0][0]
        for i in range (k) :
            answer = heapq.heappop(q)
        
        return answer
            