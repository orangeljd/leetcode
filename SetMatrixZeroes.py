class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, column = len(matrix), len(matrix[0])
        zeroRow, zeroColumn = [0 for i in range(row)], [0 for i in range(column)]
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    zeroRow[i] = 1
                    zeroColumn[j] = 1
        for index, n in enumerate(zeroRow):
            if n == 1:
                for j in range(column):
                    matrix[index][j] = 0
        for index, n in enumerate(zeroColumn):
            if n == 1:
                for i in range(row):
                    matrix[i][index] = 0
        return

t = Solution()
t.setZeroes([[0, 1]])