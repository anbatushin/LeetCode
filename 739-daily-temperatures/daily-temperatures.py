class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            count = 0
            while len(stack) != 0 and temperatures[i] >= stack[-1][0]:
                count += stack[-1][1]
                stack.pop()
            if len(stack) != 0:
                count += 1
            else:
                count = 0
            stack.append((temperatures[i], count))
            res[i] = count
        return res
