class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        nbones=0
        for x in s:
            if x=="1":
                nbones+=1
        nbones-=1
        return "1"*nbones+"0"*(len(s)-nbones-1)+"1"