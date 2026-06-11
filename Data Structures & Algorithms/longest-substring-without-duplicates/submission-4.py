class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        e = 0
        maxd = 0

        seen = set()

        while e < len(s):

            if s[e] not in seen:
                seen.add(s[e])
                maxd = max(maxd, e - i + 1)
                e += 1
            else:
                seen.remove(s[i])
                i += 1

        return maxd