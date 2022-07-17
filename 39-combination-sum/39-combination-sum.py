class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []
        
        def dfs(sum_val, start, use_list) :
            
            if sum_val < 0 :
                return
                
            if sum_val == 0 :
                answer.append(use_list)
                return
            
            elif sum_val > 0 :
                for i in range(start, len(candidates)) :
                    dfs(sum_val - candidates[i], i, use_list+ [candidates[i]])
        
        
        dfs(target, 0, [])
        
        return answer
                