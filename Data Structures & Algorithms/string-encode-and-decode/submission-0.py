class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"*"+s
        return res

    def decode(self, s: str) -> List[str]:
        idx=0
        res=[]
        while idx<len(s):
            start=idx
            while s[idx]!="*":
                idx+=1
            n=int(s[start:idx])
            idx+=1
            res.append(s[idx:idx+n])
            idx+=n
        return res