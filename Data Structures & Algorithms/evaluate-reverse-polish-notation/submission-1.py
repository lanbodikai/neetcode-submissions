class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                top = stack.pop()
                second = stack.pop()
                stack.append(top + second)
            elif i == "-":
                top = stack.pop()
                second = stack.pop()
                stack.append(second - top)
            elif i == "*":
                top = stack.pop()
                second = stack.pop()
                stack.append(top * second)
            elif i == "/":
                top = stack.pop()
                second = stack.pop()
                stack.append(int(second / top))
            else:
                stack.append(int(i))
        
        return stack.pop()