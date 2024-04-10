class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_m = 0
        right_m = len(matrix)
        while left_m < right_m:
            index_med = (left_m + right_m) // 2
            if matrix[index_med][0] == target:
                return True
            elif matrix[index_med][0] < target:
                left_m = index_med + 1
            else:
                right_m = index_med
        if left_m == 0:
            return False
        else:
            index_med = left_m - 1
        left_n = 0
        right_n = len(matrix[0])
        while left_n < right_n:
            med = (left_n + right_n) // 2
            # print(matrix[index_med][med])
            if matrix[index_med][med] == target:
                return True
            elif matrix[index_med][med] < target:
                left_n = med + 1
            else:
                right_n = med
        return False