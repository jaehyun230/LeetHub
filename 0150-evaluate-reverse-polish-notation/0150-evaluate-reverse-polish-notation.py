class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashMap = {"+":add, "-":sub, "*":mul, "/":lambda a,b: int(a/b)}
        stack = []
        for token in tokens:
            if token in hashMap:
                b = stack.pop()
                a = stack.pop()
                c = hashMap[token](a, b)
            else:
                c = int(token)
            stack.append(c)
        return stack[-1]