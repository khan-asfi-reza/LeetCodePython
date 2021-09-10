class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inverse = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for each in s:
            if each in inverse:
                if stack and stack[-1] == inverse[each]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(each)

        return True if not stack else False
