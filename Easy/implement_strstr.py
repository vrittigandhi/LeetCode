class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        a = ""
        if needle != "" and needle in haystack:
            a = haystack.index(needle)
        
        if a != "":
            return a
        elif needle == "":
            return 0
        else:
            return -1
