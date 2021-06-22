class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        elif x < 0:
            return False
        temp = x
        res = 0
        while temp:
            res += temp%10
            temp //= 10
            res *= 10
        res //= 10
        if res == x:
            return True
        return False
