class Solution:
    def calc(self, s: str) -> int:
        """ calc simple math without () """
        stack = []
        op = "+"
        for tok in re.findall(r"\d+|[-+*]", s):
            if tok.isnumeric():
                if op == "+":
                    stack.append(int(tok))
                elif op == "-":
                    stack.append(-int(tok))
                elif op == "*":
                    stack.append(stack.pop() * int(tok))
            else:
                op = tok
        return sum(stack)
    
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        while True:
            # deal with most inner (...) each time
            sub = re.search("\([^()]+\)", s)
            if not sub:
                break
            subexp = sub.group(0)
            subval = self.calc(subexp[1:-1])
            s = s.replace(subexp, str(subval))
            if subval < 0:
                s = s.replace("--", "+")  # "1-(-2)" tyope of case
        return self.calc(s)