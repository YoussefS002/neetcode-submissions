class Solution:
    def reverse(self, x: int) -> int:
        L=[]
        ss=int(str(abs(x))[::-1])
        while ss:
            L.append(ss%2)
            ss//=2
        if len(L)>=32:
            return 0
        if x>=0:
            return int(str(x)[::-1])
        else:
            return - int(str(x)[1:][::-1])