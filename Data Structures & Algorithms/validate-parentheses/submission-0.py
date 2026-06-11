class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"[" : "]", "{" : "}", "(" : ")"}

        stk = []

        for i in s:
            if i in dic:
                stk.append(i)
            else:
                if not stk:
                    return False
                
                top = stk.pop()

                if dic[top] != i:
                    return False
            
        
        return len(stk) == 0
