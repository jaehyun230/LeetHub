class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        answer = []
        
        def dfs(csum, start, use):
            if csum < 0:
                return
            elif csum == 0:
                answer.append(use)
                return
            # If no duplicates were allowed, dfs would pass i+1 instead
            for i in range(start,len(candidates)):
                dfs(csum-candidates[i], i, use+[candidates[i]])

        dfs(target,0,[])
        
        return answer