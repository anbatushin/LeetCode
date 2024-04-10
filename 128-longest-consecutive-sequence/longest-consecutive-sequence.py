class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                count = 0
                while num + count in nums_set:
                    count += 1
                max_len = max(count, max_len)
        return max_len