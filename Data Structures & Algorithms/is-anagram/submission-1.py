class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss={}
        tt={}
        for c in s:
            ss[c]=ss.get(c, 0)+1
        for c in t:
            tt[c]=tt.get(c, 0)+1
        return ss==tt