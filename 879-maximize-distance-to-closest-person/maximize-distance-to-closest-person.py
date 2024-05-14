class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        left = -1
        res = 0

        for i in range(len(seats)):
            if seats[i] == 1:
                if left == -1:
                    res = i
                else:
                    res = max(res, (i - left) // 2)
                left = i

        return max(res, len(seats) - left - 1)