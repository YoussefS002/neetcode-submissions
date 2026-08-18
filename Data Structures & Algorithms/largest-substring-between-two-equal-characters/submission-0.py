class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        begin = {}
        end= {}
        for i in range(len(s)):
            if s[i] not in begin:
                begin[s[i]]=i
        for i in range(len(s)):
            end[s[i]]=i  
        res=-1
        for c in begin:
            if c in end:
                res=max(res, end[c]-begin[c]-1)
        return res