class Solution:
    def isValid(self, s: str) -> bool:
        para = {"}":"{", ")":"(", "]":"["}

        stack = []
        stack.append("1")

        for i in s:
            if i not in para:
                stack.append(i)
            else:
                if stack[-1] == para[i]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 1