class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}
        for i in range(len(s)):
            letter = s[i]
            if letter in s_dict:
                s_dict[letter]+=1
            else:
                s_dict[letter]=1
        for i in range(len(t)):
            letter = t[i]
            if letter in t_dict:
                t_dict[letter]+=1
            else:
                t_dict[letter]=1
        if len(s_dict) != len(t_dict):
            return False
        for letter in s_dict:
            if letter not in t_dict or t_dict[letter] != s_dict[letter]:
                return False
        return True