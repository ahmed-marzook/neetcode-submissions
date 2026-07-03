class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"(":")","{":"}","[":"]"}
        if not(s[0] in parentheses.keys()) or len(s) % 2 != 0:
            return False
        close_parentheses = []
        for c in s:
            if c in parentheses.keys():
                close_parentheses.append(parentheses[c])
            elif c in parentheses.values():
                if len(close_parentheses) > 0 and c == close_parentheses[-1]:
                    close_parentheses.pop()
                else:
                    return False
        return not(close_parentheses)