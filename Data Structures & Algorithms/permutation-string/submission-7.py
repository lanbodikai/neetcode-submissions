class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)

        i = 0
        e = len(s1)

        while e <= len(s2):
            window = s2[i:e]

            if Counter(window) == count:
                return True
            
            i += 1
            e += 1
        
        return False
            