class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                continue
            else:
                left += 1
                nums[left] = nums[index]
        return left + 1