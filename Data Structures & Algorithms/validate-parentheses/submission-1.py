class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stackChar = { ")": "(", "]": "[", "}": "{" }

        for char in s:
            if char in stackChar:
                if stack and stack[-1] == stackChar[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack