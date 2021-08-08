class Solution:
    def __init__(self,grid,rows,col):
        self.grid = grid
        self.rows = rows
        self.col = col
    def numIslands(self):
        count = 0
        for x in range(0,self.rows):
            for y in range(0,self.col):
                if(grid[x][y]==1):
                    count = count + 1
                    self.dfs(x,y)
        return count

    def dfs(self,x,y):
            if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid[0]) or self.grid[x][y] != 1:
                return

            self.grid[x][y] = 2
            self.dfs(x - 1, x - 1)
            self.dfs(x - 1, y)
            self.dfs(x - 1, x + 1)
            self.dfs(x, y - 1)
            self.dfs(x, y + 1)
            self.dfs(x + 1, y - 1)
            self.dfs(x + 1, y)
            self.dfs(x + 1, y + 1)

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
rows = len(grid)
col = len(grid[0])
s = Solution(grid,rows,col)

print(s.numIslands())
