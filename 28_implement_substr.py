class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle or not needle:
            return 0

        n = len(haystack)
        m = len(needle)
        for i in range(n):
            k = i + m
            if k > n:
                k = i + 1
            if haystack[i: k] == needle:
                return i

        return -1



