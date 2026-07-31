class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp1 = ""
        temp2 = ""
        for i in s:
            if i.isalnum():
                temp1 += i


        for i in reversed(s):
            if i.isalnum():
                temp2 += i

        return temp1 == temp2