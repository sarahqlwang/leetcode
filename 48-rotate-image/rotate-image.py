class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 1. transpose
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. reverse
        def reverse(row):
            l = 0
            r = n-1
            while l<r:
                row[l],row[r] = row[r], row[l]
                l+=1
                r-=1

        for row in matrix:
            reverse(row)
