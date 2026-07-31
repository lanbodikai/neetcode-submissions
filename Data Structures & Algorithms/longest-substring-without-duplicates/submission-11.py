class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        i = 0
        e = 0
        n = len(s)
        longest = 0

        while e < n:
            if s[e] not in seen:
                seen.add(s[e])
                longest = max(longest, e - i + 1)
                e += 1        

            else:
                seen.remove(s[i])
                i += 1

        return longest