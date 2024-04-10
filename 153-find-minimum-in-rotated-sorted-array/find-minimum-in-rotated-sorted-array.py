class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            med = (left + right) // 2
            if nums[med] < nums[right]:
                right = med
            else:
                left = med + 1
        return nums[right]