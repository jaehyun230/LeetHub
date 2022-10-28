class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        
        for string in strs :
            
            sort_str = sorted(string)
            now_str = "".join(sort_str)
            
            if now_str not in dic :
                dic[now_str] = []
            
            dic[now_str].append(string)
        
        return list(dic.values())