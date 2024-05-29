class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k
        while l < r:
            med = (l + r) // 2
            if x - arr[med] > arr[med + k] - x:
                l = med + 1
            else:
                r = med
        return arr[l:l + k]