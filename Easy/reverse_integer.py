class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            temp = x
        else:
            temp = x*(-1)
        res = 0
        
        while temp:
            res += temp%10
            temp //= 10
            res *= 10
        res //= 10
        if 0 <= res <= ((2**31)-1):
            if x >= 0:
                return res
            else:
                return res*(-1)
        else:
            return 0
