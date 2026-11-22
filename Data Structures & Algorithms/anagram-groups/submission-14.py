class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ma = {}
        res = []
        for string in strs:
            sort = (",").join(sorted(string))
            if sort in ma:
                ma[sort].append(string)
            else:
                ma[sort] = [string]
        
        for i in ma.values():
            res.append(i)
        
        return res