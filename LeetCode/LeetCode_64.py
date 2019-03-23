class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j >= 1:
                    grid[i][j] += grid[i][j - 1]
                elif i == 0 and j == 0:
                    continue
                elif i >= 1 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[i-1][j-1]
