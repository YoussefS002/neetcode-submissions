class Solution:
    def numDecodings(self, s: str) -> int:
        memo=[[None for r in range(len(s))] for l in range(len(s))]
        def aux(l, r, attached=False):
            if memo[l][r] is not None:
                return memo[l][r]
            length=r-l+1
            if length==1:
                if s[l]=="0":
                    return 0
                return 1
            if length==2:
                if s[l]=="0":
                    return 0
                if s[r]=="0":
                    if s[l]=="1" or s[l]=="2":
                        return 1
                    else:
                        return 0
                else:
                    if attached:
                        if 10<=int(s[l:r+1])<=26:
                            return 1
                        else:
                            return 0
                    else:
                        if 10<=int(s[l:r+1])<=26:
                            return 2
                        else:
                            return 1
            memo[l][r] = aux(l, l) * aux(l+1, r) + aux(l, l+1, attached=True) * aux(l+2, r)
            return memo[l][r]
        return aux(0, len(s)-1)


