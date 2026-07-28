class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ma = {}
        for i in strs:
            b = tuple(sorted(i))
            if b in ma:
                ma[b].append(i)
            else:
                ma[b] = [i]
        
        return list(ma.values())