class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts={}
        for i in range(len(strs)):
            counts[i]={}
            for c in strs[i]:
                counts[i][c]=counts[i].get(c, 0)+1
        indexes=set(range(len(strs)))
        res=[]
        while indexes:
            idx=indexes.pop()
            res.append([strs[idx]])
            to_remove=set()
            for idx2 in indexes:
                if counts[idx2]==counts[idx]:
                    to_remove.add(idx2)
                    res[-1].append(strs[idx2])
            indexes=indexes-to_remove
        return res