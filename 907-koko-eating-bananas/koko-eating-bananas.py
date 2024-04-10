class Solution:
    @staticmethod
    def sumEat(piles: list[int], k: int) -> int:
        return sum([math.ceil(pile / k) for pile in piles])

    @staticmethod
    def minEatingSpeed(piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_med = max(piles)
        while left < right:
            med = (left + right) // 2
            # print(Solution.sumEat(piles, med), med)
            # print(left, right, med)
            if Solution.sumEat(piles, med) > h:
                left = med + 1
            else:
                min_med = min(min_med, med)
                right = med
        return min_med
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
        