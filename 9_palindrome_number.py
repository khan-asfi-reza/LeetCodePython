class Solution:

    def reverse(self, x: int) -> int:
        sign = 1

        if x < 0:
            sign = -1
            x *= sign

        summation = 0

        while x:
            remainder = x % 10
            summation = summation * 10 + remainder
            x //= 10

        summation *= sign

        if not -2147483648 < summation < 2147483647:
            return 0

        return summation

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if self.reverse(x) == x:
            return True
