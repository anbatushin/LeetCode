class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pref = [1] * (length + 2)
        suff = [1] * (length + 2)
        for i in range(len(nums)):
            pref[i + 1] = nums[i] * pref[i]
            suff[length - i] = nums[length - i - 1] * suff[length - i + 1]
        for i in range(length):
            nums[i] = pref[i] * suff[i + 2]
        return nums