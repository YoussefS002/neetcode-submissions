class Solution:
    def longestPalindrome(self, s: str) -> str:
        starting_index=0
        length=1
        for i in range(len(s)):
            l, r = i-1, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1 > length:
                length=r-l-1
                starting_index=l+1
            
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1 > length:
                length=r-l-1
                starting_index=l+1
        return s[starting_index:starting_index+length]