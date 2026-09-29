class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in parentheses:
                value = parentheses.get(char);
                if stack and value == stack[-1]:
                    stack.pop();
                else:
                    return False
            else:
                stack.append(char);
        if stack:
            return False
        else:
            return True