class Solution:
    def isValid(self, s: str) -> bool:
        para = {"}":"{", ")":"(", "]":"["}

        stack = []

        for i in s:
            if i not in para:
                stack.append(i)
            else:
                if stack and stack[-1] == para[i]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0