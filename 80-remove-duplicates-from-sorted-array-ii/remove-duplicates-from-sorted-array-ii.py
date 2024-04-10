class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        dups = 0
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                if dups == 1:
                    continue
                else:
                    dups += 1
                    left += 1
                    nums[left] = nums[index]
            else:
                dups = 0
                left += 1
                nums[left] = nums[index]
        print(nums)
        return left + 1