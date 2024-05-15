class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        right = 0

        while left < len(nums):
            if nums[left] == 0:
                while right < len(nums) and nums[right] == 0:
                    right += 1
                if right == len(nums):
                    break
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right = left

        # print(nums)
