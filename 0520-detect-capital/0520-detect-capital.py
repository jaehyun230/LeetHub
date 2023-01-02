class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        for i in range(0, len(word)):
            if ord(word[0]) in range(97, 123):
                return all(ord(word[i]) in range(97, 123) for i in range(0, len(word)))
            else:
                if all(ord(word[i]) in range(65, 91) for i in range(0, len(word))):
                    return True
                elif all(ord(word[i]) in range(97, 123) for i in range(1, len(word))):
                    return True
                else:
                    return False