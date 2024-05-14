class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        right = 0
        maxres = 0
        count = 0

        while right < len(nums):
            if nums[right] == 0:
                count += 1
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            maxres = max(maxres, right - left)
            right += 1

        return maxres
