class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        pref = []
        sum = 0
        for i in range(len(nums)):
            pref.append(sum + nums[i])
            sum += nums[i]

        adds = {0: 1}
        res = 0
        for i in range(len(nums)):
            if pref[i] - k in adds:
                res += adds[pref[i] - k]
            adds[pref[i]] = adds.get(pref[i], 0) + 1

        return res