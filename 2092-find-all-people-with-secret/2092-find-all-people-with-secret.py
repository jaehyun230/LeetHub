class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v, time in meetings:
            adj[u].append([time, v])
            adj[v].append([time, u])
        s = [(0, firstPerson),(0,0)]
        secret = set([firstPerson, 0])
        visited = set()
        while s:
            t, u = heapq.heappop(s)
            if u in visited:
                continue
            visited.add(u)
            for t2, v in adj[u]:
                if t2 >= t and v not in visited:
                    secret.add(v)
                    heapq.heappush(s,(t2, v))
            if len(visited) == n:
                break
        return list(secret)