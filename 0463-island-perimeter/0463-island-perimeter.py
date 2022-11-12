class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        # row, col
        def dfs(r, c):
            # grid가 칸 밖으로 나갔거나
            # grid가 water면
            # return 1
            if r < 0 or r >= N or c < 0 or c >= M or grid[r][c] == 0:
                return 1
            
            if grid[r][c] == 1:
                # 방문했으니 2
                grid[r][c] = 2
                # 상하좌우
                return dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

            return 0
        
        res = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    res += dfs(r, c)

        return res