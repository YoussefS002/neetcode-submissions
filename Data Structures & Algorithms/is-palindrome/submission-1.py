class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw_s = ""
        for i in range(len(s)):
            l = s[i]
            if l.isalnum():
                raw_s+=l.lower()
        return raw_s == raw_s[::-1]