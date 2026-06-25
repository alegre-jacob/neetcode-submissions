class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '{([':
                stack.append(c)
            else:
                try:
                    if c == '}' and stack.pop() != '{':
                        return False
                    elif c == ']' and stack.pop() != '[':
                        return False
                    elif c == ')' and stack.pop() != '(':
                        return False
                except:
                    return False;
        if len(stack) == 0:
            return True
        return False