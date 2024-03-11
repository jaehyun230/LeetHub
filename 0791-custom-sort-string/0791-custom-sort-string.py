class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]]=i
        
        result_arr = []
        for i in range(len(s)):
            heapq.heappush(result_arr, (order_dict.get(s[i],27), s[i]))
        
        ans=""
        while result_arr:
            _, char = heapq.heappop(result_arr)
            ans += char
        return ans