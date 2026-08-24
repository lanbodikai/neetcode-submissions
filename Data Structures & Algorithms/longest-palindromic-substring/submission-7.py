class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        for i in range(len(s)):
            if i - 1 >= 0 and i + 1 < len(s) and s[i - 1] == s[i + 1]:
                left = i
                right = i
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > len(result):
                        result = s[left:right + 1]
                
                    left -= 1
                    right += 1
            if i + 1 < len(s) and s[i] == s[i + 1]:
                left = i
                right = i + 1

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > len(result):
                        result = s[left:right + 1]
                
                    left -= 1
                    right += 1
            
        return result
