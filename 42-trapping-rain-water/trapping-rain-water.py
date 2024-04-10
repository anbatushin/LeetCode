class Solution:
    def trap(self, height: List[int]) -> int:
        max_index = 0
        for index in range(len(height)):
            if height[index] > height[max_index]:
                max_index = index
        res = 0
        curr_max = 0
        for index in range(max_index):
            curr_max = max(curr_max, height[index])
            res += curr_max - height[index]
        curr_max = 0
        for index in range(len(height) - 1, max_index, -1):
            curr_max = max(curr_max, height[index])
            res += curr_max - height[index]
        return res