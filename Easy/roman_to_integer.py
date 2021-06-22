class Solution:
    def romanToInt(self, s: str) -> int:
        dic1 = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = 0
        for i in range(len(s)-1):
            if dic1[s[i]] < dic1[s[i+1]]:
                result -= dic1[s[i]]
            else:
                result += dic1[s[i]] 
        result += dic1[s[-1]]
        return result
