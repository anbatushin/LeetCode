class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if n <= k:
            return arr
        if x < arr[0]:
            return arr[:k]
        if x > arr[n - 1]:
            return arr[n - k:]
        
        l = 0
        r = n - k
        while l < r:
            med = (l + r) // 2
            if x - arr[med] > arr[med + k] - x:
                l = med + 1
            else:
                r = med
        return arr[l:l + k]