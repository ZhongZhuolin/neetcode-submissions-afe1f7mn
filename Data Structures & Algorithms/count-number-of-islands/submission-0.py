class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col, rows = len(grid), len(grid[0])
        num_islands = 0

        def get_rid(i, j):
            if i < 0 or i >= col or j < 0 or j >= rows or grid[i][j] == '0':
                return
            else:
                grid[i][j] = '0'
                get_rid(i+1, j)
                get_rid(i-1, j)
                get_rid(i, j+ 1)
                get_rid(i, j-1)


        for i in range(col):
            for j in range(rows):
                if grid[i][j] == '1':
                    num_islands += 1
                    get_rid(i, j)
        return num_islands
