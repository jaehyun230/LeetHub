class Solution:
    def numDecodings(self, s: str) -> int:
        def search(s, memo):
            if s in memo:
                return memo[s]
            if len(s) <= 1:
                return 1 if s != "0" else 0
            res, n, i = 0, len(s), 1
            while i <= n and 1 <= int(s[:i]) <= 26:
                res += search(s[i:], memo)
                i += 1
            memo[s] = res
            return res

        if s == "":
            return 0
        return search(s, {})