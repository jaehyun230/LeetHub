class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPal(word):
            return word == word[::-1]
        palPairs = []
        wordDict = {}
        for i, word in enumerate(words):
            wordDict[word] = i
        for i, word in enumerate(words):
            for j in range(0, len(word)):
                prefix, suffix = word[:j], word[j:] # find all suffix and prefix
                if prefix[::-1] in wordDict and wordDict[prefix[::-1]] != i and isPal(suffix):
                    palPairs.append([i, wordDict[prefix[::-1]]]) # check if reverse prefix in dict and suffix palindrome
                if suffix[::-1] in wordDict and wordDict[suffix[::-1]] != i and isPal(prefix):
                    palPairs.append([wordDict[suffix[::-1]], i]) # check if reverse suffix in dict and prefix palindrome
                if len(palPairs) > 0 and words[palPairs[-1][1]] == '': # tricky part for prefix or suffix is ''. for example, if '1' + '' is palindrome, then '' + '1' should also be palindrome. and add '' + '1' manually
                    pair = palPairs[-1]
                    palPairs.append([pair[1], pair[0]])
        return palPairs