class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for tok in tokens:
            if tok == '+' or tok == '-' or tok == '*' or tok == '/':
                sec = int(s.pop())
                fir = int(s.pop())
                if tok == '+':
                    s.append(fir + sec)
                elif tok == '-':
                    s.append(fir - sec)
                elif tok == '*':
                    s.append(fir * sec)
                else:
                    s.append(fir / sec)
            else:
                s.append(tok)
        return int(s[0])