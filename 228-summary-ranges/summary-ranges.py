class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        res = []
        begin = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                if nums[i - 1] != begin:
                    res.append(str(begin) + '->' + str(nums[i - 1]))
                else:
                    res.append(str(begin))
                begin = nums[i]

        if nums[-1] != begin:
            res.append(str(begin) + '->' + str(nums[-1]))
        else:
            res.append(str(begin))
            
        return res
