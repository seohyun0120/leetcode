class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        N = len(image)
        M = len(image[0])
        cur_color = image[sr][sc]
        
        def dfs(r, c):
            # 범위 밖에 있지않고
            # 주어진 색상과 같고
            # 방문하지 않았다면
            if 0 <= r < N and 0 <= c < M and image[r][c] == cur_color and image[r][c] != color:
                image[r][c] = color
                # 상하좌우 움직임
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
            
        dfs(sr, sc)
        return image
            