# LeetCode N329, Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        dp = [[-1]*m for _ in range(n)]
        answer = 0

        def dfs(x,y,res): # 백트래킹으로 풀어보고싶었는데 실패한 모습이다..
            if 0<=x<m and 0<=y<n and dp[x][y] == -1: # 범위에서 벗어나지않고 방문하지 않은 곳이라면
                for a, b in directions: # 상하좌우 탐색
                    if 0<=x+a<m and 0<=y+b<n: 
                        if matrix[x][y] < matrix[x+a][y+b]: # 상하좌우 중 한 곳의 값이 현재보다 더 크다면
                            res.append(matrix[x+a][y+b]) # 리스트에 넣어주기
                            dfs(x+a,y+b,res) # 큰 값에 해당하는 좌표로 다시 탐색
                        else:
                            continue # 다음으로 넘어가기
                    return len(res) + 1 # 탐색이 끝나면 리스트 길이 +1로 반환(x,y좌표에 해당하는 값 포함시켜주기 위함)

        for i in range(m): # 행
            for j in range(n): # 열로 돌아가면서 dp에 넣기(를 해주고싶었다)
                dp[i][j] = dfs(i,j,[])
        # print(f'dp = {dp}')

        for k in dp: # 각 행에서 최댓값 갱신하며 찾기
            answer = max(answer,max(k))
        return answer 


# 어렵다....