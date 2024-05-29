class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        diags = collections.defaultdict(list)

        for i in range(n):
            for j in range(m):
                diags[i - j].append(mat[i][j])

        for diag in diags.values():
            diag.sort(reverse=1)

        for i in range(n):
            for j in range(m):
                mat[i][j] = diags[i-j].pop()

        return mat
        
