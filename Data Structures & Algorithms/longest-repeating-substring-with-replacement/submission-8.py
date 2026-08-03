class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frq = {}
        i = 0
        start = 0
        n = len(s)
        maxcount = 0
        result = 0

        while i < n:
            curr = s[i]
            frq[curr] = frq.get(curr, 0) + 1
            maxcount = max(maxcount, frq[curr])
            while i - start + 1 - maxcount > k:
                frq[s[start]] -= 1
                start += 1
            result = max(result, i - start + 1)
            i += 1
        
        return result
