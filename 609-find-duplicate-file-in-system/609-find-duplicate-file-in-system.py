from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        answer = []
        dic = defaultdict(list)
        
        for path in paths:
            path = path.split()
            root = path[0]
            for i in range(1,len(path)):
                file, content = path[i].split('(')
                dic[content[:-1]].append(root+'/'+file)
            
        for duplicate in dic:
            if len(dic[duplicate]) > 1:
                answer.append(dic[duplicate])
        return answer