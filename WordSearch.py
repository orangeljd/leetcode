class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        height, width = len(board), len(board[0])
        dp = [[False for j in range(width)] for i in range(height)]
        for i in range(height):
            for j in range(width):
                if self.verify(board, height, width, i, j, word, dp): return True
        return False

    def verify(self, grid, height, width, row, column, word, dp):
        if word == "": return True
        exist = False
        if grid[row][column] == word[0]:
            if len(word) == 1: return True
            else:
                dp[row][column] = True
                if column + 1 < width and not dp[row][column + 1]: exist |= self.verify(grid, height, width, row, column + 1, word[1:], dp)
                if not exist and row + 1 < height and not dp[row + 1][column]: exist |= self.verify(grid, height, width, row + 1, column, word[1:], dp)
                if not exist and column > 0 and not dp[row][column - 1]: exist |= self.verify(grid, height, width, row, column - 1, word[1:], dp)
                if not exist and row > 0 and not dp[row - 1][column]: exist |= self.verify(grid, height, width, row - 1, column, word[1:], dp)
                dp[row][column] = False
        return exist

t = Solution()
print(t.exist([['a', 'b']], "ba"))