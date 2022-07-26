# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        def dfs(grid, i, j):
            # Q. 왜 grid[i][j]!='1'를 안넣으면 에러가 날까
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!='1':
                return
            grid[i][j] = 'visited' # 방문처리
            
            # 상하좌우에서 섬찾기
            dfs(grid, i+1, j)
            dfs(grid, i, j+1)
            dfs(grid, i-1, j)
            dfs(grid, i, j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': # 섬이 있으면 dfs 진행
                    dfs(grid, i, j)
                    count += 1
        return count