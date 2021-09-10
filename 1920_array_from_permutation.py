from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + n*(nums[nums[i]] % n)

        for j in range(n):
            nums[j] = nums[j] // n

        return nums
