class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1

        return i + 1
