class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                else:
                    num = board[row][col]
                    if (num in rows[row]
                            or num in cols[col]
                            or num in grid[row // 3 * 3 + col // 3]):
                        # print(num, rows, cols, grid)
                        rows.clear()
                        cols.clear()
                        grid.clear()
                        return False
                    else:
                        rows[row].add(num)
                        cols[col].add(num)
                        grid[row // 3 * 3 + col // 3].add(num)
        # print(rows, cols, grid)
        return True