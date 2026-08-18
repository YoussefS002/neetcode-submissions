class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        L=[]
        for c in abbr:
            if c.isalpha():
                L.append(c)
            else:
                if L and L[-1].isnumeric():
                    L[-1]+=c
                else:
                    L.append(c)
        ss=""
        for x in L:
            if x.isalpha():
                ss=ss+x
            else:
                if x[0]=='0':
                    return False   
                ss=ss+'#'*int(x)
        if len(ss)!=len(word):
            return False
        for i in range(len(word)):
            if ss[i]!='#' and ss[i]!=word[i]:
                return False
        return True