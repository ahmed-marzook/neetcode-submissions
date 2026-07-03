class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"(":")","{":"}","[":"]"}
        close_parentheses_stack = []
        for c in s:
            if c in parentheses:
                close_parentheses_stack.append(parentheses[c])
            elif close_parentheses_stack and c == close_parentheses_stack[-1]:
                    close_parentheses_stack.pop()
            else:
                return False
        return not(close_parentheses_stack)