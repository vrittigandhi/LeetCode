class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        a = ""
        l = 0
        
        for j in s:
            if j not in a:
                a += j
            else:
                s = s[s.index(j)+1:]
                a = s[0:s.index(j)+1]
            new_l = len(a)
            if new_l > l:
                l = new_l
        return l
