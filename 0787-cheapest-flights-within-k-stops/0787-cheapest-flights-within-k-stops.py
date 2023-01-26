class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)   # key is 'from', value is '(to, price)'
        for from_node, to_node, price in flights:
            graph[from_node].append((to_node, price))
        
        # best-first search/dijkstra (allowing duplicate visit if previous visits do not meet stop requirement)
        heap = [(0, -1, src)]   # (cost, stop, node)
        min_k = defaultdict(lambda: float('inf'))
        min_k[src] = 0
        while heap:
            cost, stop, node = heapq.heappop(heap)
            if min_k[node] < stop:  # ignore the path if less-stop path exist
                continue
            min_k[node] = stop
            # check if node is destination
            if node == dst:
                return cost
            # update neighbors
            for to_node, to_cost in graph[node]:
                if stop+1 <= k:
                    heapq.heappush(heap, (cost+to_cost, stop+1, to_node))
                    
        return -1