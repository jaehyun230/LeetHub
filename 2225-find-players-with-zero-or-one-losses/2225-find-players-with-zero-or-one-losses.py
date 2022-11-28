from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        win_dic = defaultdict(int)
        lose_dic = defaultdict(int)
        
        for winner, loser in matches :
            win_dic[winner] +=1
            lose_dic[loser] +=1
        
        answer = [[], []]
        
        for win in win_dic :
            if lose_dic[win] == 0 :
                answer[0].append(win)
        
        for lose in lose_dic :
            if lose_dic[lose] == 1 :
                answer[1].append(lose)
        
        answer[0].sort()
        answer[1].sort()
        
        return answer