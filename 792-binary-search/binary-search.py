class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            med = (left + right) // 2
            if nums[med] == target:
                return med
            elif nums[med] < target:
                left = med + 1
            else:
                right = med
        return -1