class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        
        for n in arr:
            dic[n] += 1
            
        check_dic = defaultdict(int)
        for key in dic:
            check_dic[dic[key]] += 1
            # not unique
            if check_dic[dic[key]] == 2:
                return False
            
        return True