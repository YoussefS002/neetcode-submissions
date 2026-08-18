class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {}
        for i in range(len(s)):
            last_occurence[s[i]]=i
        idx=0
        res=[]
        while idx<len(s):
            first_idx=idx
            last_idx=last_occurence[s[idx]]
            while idx<last_idx:
                idx+=1
                last_idx=max(last_idx, last_occurence[s[idx]])
            res.append(last_idx-first_idx+1)
            idx=idx+1
        return res