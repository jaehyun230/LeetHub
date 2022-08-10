from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = [0] * len(arr)
        if start >= len(arr) :
            return False
        
        visited[start] = 1
        
        q = deque()
        q.append(start)
        
        while q :
            now = q.popleft()
            
            if arr[now] == 0 :
                return True
            
            if 0 <= now - arr[now] and visited[now-arr[now]] == 0 :
                visited[now-arr[now]] = 1
                q.append(now-arr[now])
            
            if now + arr[now] < len(arr) and visited[now + arr[now]] == 0 :
                visited[now + arr[now]] = 1
                q.append(now+ arr[now])
        
        return False