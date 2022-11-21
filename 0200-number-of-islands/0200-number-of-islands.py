class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j, m , n)
                    ans += 1
        
        return ans

    def dfs(self, grid, r, c, m, n):
        if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != "1":
            return

        grid[r][c] = "2"
        self.dfs(grid, r+1, c, m, n)
        self.dfs(grid, r-1, c, m, n)
        self.dfs(grid, r, c+1, m, n)
        self.dfs(grid, r, c-1, m , n)