class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zeros = 0
        nonzeros = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                zeros += 1
            else:
                nums[nonzeros] = nums[index]
                nonzeros += 1

        for i in range(zeros):
            nums[nonzeros] = 0
            nonzeros += 1
