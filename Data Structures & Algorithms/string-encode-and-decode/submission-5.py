class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            length = len(i)
            encode = encode + str(len(i)) + "#" + i
        
        return encode
    def decode(self, s: str) -> List[str]:
        res = []


        i = 0
        n = len(s) - 1
        
        while i <= n:
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            start = j + 1
            end = start + length

            res.append(s[start:end])

            i = end
        
        return res
        
