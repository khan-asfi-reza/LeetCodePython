"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


def solution(s: str) -> int:
    max_len = 0
    start_point = 0
    hashMap = dict()

    for key, val in enumerate(s):
        if val in hashMap and hashMap[val] >= start_point:
            start_point = hashMap[val] + 1

        else:
            max_len = max(max_len, key - start_point + 1)

        hashMap[val] = key

    return max_len


# Extra Find Longest SubString
def longest_substring(s: str) -> str:
    max_len = 0
    start_point = 0
    hashMap = dict()

    for key, val in enumerate(s):
        if val in hashMap and hashMap[val] >= start_point:
            start_point = hashMap[val] + 1

        else:
            max_len = max(max_len, key - start_point + 1)

        hashMap[val] = key

    return s[start_point - 1: start_point + max_len - 1]




