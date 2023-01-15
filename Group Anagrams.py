class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m=defaultdict(list)
        for i in strs:
            x=''.join(sorted(i))
            m[x].append(i)
        res=[]
        for k in m:
            res.append(m[k])
        return res
