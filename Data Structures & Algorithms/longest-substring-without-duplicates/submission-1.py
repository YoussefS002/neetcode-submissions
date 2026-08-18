class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_pos = {}
        best_length = 0
        l=0
        for r in range(len(s)):
            c=s[r]
            
            if c in char_pos and char_pos[c]>=l:
                l=char_pos[c]+1
            char_pos[c]=r
            best_length=max(best_length, r-l+1)
            
        return best_length