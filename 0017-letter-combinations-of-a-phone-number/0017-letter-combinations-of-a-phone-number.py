class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        
        datas = list(digits)
        
        def backtrack(combi, index) :
            if index >= len(datas) :
                res.append(combi)
            else :
                for i in phone[digits[index]] :
                    backtrack(combi + i, index+1)
        
        backtrack("", 0)
        
        return res