class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            n = len(i)
            res += str(n) + "#" + str(i)
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        e = 1
        n = len(s)
        res = []

        while e < n:
            if s[e] == "#":
                num = int(s[i:e])
                word = s[e + 1:e + 1 + num]
                res.append(word)
                i = e + num + 1
                e = i + 1
            else:
                e += 1
        
        return res
