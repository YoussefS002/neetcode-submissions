class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw_s = ""
        for i in range(len(s)):
            l = s[i]
            if l.isalnum():
                raw_s+=l.lower()
        l=0
        r=len(raw_s)-1
        while l<r:
            if raw_s[l] != raw_s[r]:
                return False
            l+=1
            r-=1
        return True