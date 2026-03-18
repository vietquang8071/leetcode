from typing import List
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        prefix = [[0] * cols for _ in range(rows)]
        prefix[0][0] = grid[0][0]
        for j in range(1, cols):
            prefix[0][j] = prefix[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            prefix[i][0] = prefix[i - 1][0] + grid[i][0]

        for i in range(1, rows):
            for j in range(1, cols):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] + grid[i][j] - prefix[i - 1][j - 1]
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if prefix[i][j] <= k:
                    count += 1
        return count