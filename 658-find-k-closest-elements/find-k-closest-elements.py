class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def bin_search_position(arr, n, x):
            l = 0
            r = n - 1
            while l <= r:
                med = (l + r) // 2
                if arr[med] < x:
                    l = med + 1
                elif arr[med] > x:
                    r = med - 1
                else:
                    return med
            return r

        n = len(arr)
        if n <= k:
            return arr
        if x < arr[0]:
            return arr[:k]
        if x > arr[n - 1]:
            return arr[n-k:]
        
        index = bin_search_position(arr, n, x)
        print(index, arr[index])
        if index < n - 1 and x - arr[index] > arr[index + 1] - x:
            index += 1

        left = index
        right = index
        count = 1
        while count < k:
            if left > 0 and right < n - 1:
                if x - arr[left - 1] <= arr[right + 1] - x:
                    left -= 1
                else:
                    right += 1
                count += 1
            if left <= 0:
                right += k - count
                count = k
                break
            if right >= n - 1:
                left -= k - count
                count = k
                break
        print(left, right)
        return arr[left:right + 1]