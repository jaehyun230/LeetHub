import bisect
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_idx = defaultdict(list)
        for i, c in enumerate(s):
            char_idx[c].append(i)
        
        ans = 0
        for word in words:
            match = True
            prev_idx = -1
            for c in word:
                if c not in char_idx:
                    match = False
                    break
                
                char_idx_lst = char_idx[c]
                lst_idx = bisect.bisect_right(char_idx_lst, prev_idx)
                if lst_idx == len(char_idx_lst):
                    match = False
                    break
                
                prev_idx = char_idx_lst[lst_idx]
            ans += 1 if match else 0
        return ans