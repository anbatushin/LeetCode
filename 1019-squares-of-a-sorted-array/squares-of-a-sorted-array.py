class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def quicksort(nums, fst, lst):
            if fst >= lst:
                return
            left, right = fst, lst
            pivot = nums[(fst + lst) // 2]

            while left <= right:
                while nums[left] < pivot:
                    left += 1
                while nums[right] > pivot:
                    right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1

            quicksort(nums, fst, right)
            quicksort(nums, left, lst)
        
        for i in range(len(nums)):
            nums[i] *= nums[i]
        quicksort(nums, 0, len(nums) - 1)
        return nums