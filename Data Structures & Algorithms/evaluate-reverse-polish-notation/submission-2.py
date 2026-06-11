class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = ["+", "-", "*", "/"]
        for i in tokens:
            if i in symbols:
                top = stack.pop()
                second = stack.pop()
                if i == "+":
                    stack.append(top + second)
                elif i == "-":
                    stack.append(second - top)
                elif i == "*":
                    stack.append(top * second)
                else:
                    stack.append(int(second / top))
            else:
                stack.append(int(i))
        
        return stack.pop()