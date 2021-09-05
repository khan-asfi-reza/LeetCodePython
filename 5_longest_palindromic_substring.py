
def longestPalindrome(s: str) -> str:
    longest = ""
    long_len = 0

    def slide():
        nonlocal longest
        nonlocal long_len
        nonlocal left
        nonlocal right
        while s and left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > long_len:
                longest = s[left: right + 1]
                long_len = right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        left, right = i, i
        slide()
        left, right = i, i + 1
        slide()

    return longest

