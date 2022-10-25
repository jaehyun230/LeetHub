class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        result = ""
        result2 = ""
        
        for word in word1 :
            result +=word
        for word in word2 :
            result2 +=word
        
        if result == result2 :
            return True
        else :
            return False