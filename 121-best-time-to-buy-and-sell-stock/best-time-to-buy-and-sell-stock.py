class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        min_price = [prices[0]] * len(prices)
        max_price = [prices[-1]] * len(prices)
        minp = prices[0]
        maxp = prices[-1]
        left = 0
        right = len(prices) - 1

        while left <= right:
            minp = min(minp, prices[left])
            min_price[left] = minp
            left += 1

        while right >= 0:
            maxp = max(maxp, prices[right])
            max_price[right] = maxp
            right -= 1

        left = 0
        best = 0
        while left < len(prices) - 1:
            best = max(best, max_price[left + 1] - min_price[left])
            left += 1

        return best