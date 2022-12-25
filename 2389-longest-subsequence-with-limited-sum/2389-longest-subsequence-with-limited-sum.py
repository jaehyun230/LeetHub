class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        numsSorted = sorted(nums)
        res = []
		
        for q in queries:
            total = 0
            count = 0
            for num in numsSorted:
                total += num
                count += 1
                if total > q:
                    count -= 1
                    break
            res.append(count)
        
        return res