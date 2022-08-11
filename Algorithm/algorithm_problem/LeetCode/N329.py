# LeetCode N329, Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        dp = [[-1] * n for _ in range(m)]
        answer = 0

        def dfs(r,c,res): # 백트래킹으로 풀어보고싶었는데 실패한 모습이다..
            if 0<=r<m and 0<=c<n and dp[r][c] == -1: # 범위에서 벗어나지않고 방문하지 않은 곳이라면
                for a, b in directions: # 상하좌우 탐색
                    nr, nc = r+a, c+b
                    if 0<=nr<m and 0<=nc<n and matrix[r][c] < matrix[x+a][c+b]: # 상하좌우 중 한 곳의 값이 현재보다 더 크다면
                        res.append(matrix[r+a][c+b]) # 리스트에 넣어주기
                        dp[r][c] = max(dp[r][c], dfs(r+a,c+b,res)+1) # 큰 값에 해당하는 좌표로 다시 탐색
                        res.pop()
                    else:
                        continue # 다음으로 넘어가기
                dp[r][c] = len(res) + 1
                return dp[r][c] # 탐색이 끝나면 리스트 길이 +1로 반환(r,c)좌표에 해당하는 값 포함시켜주기 위함)
            return dp[r][c]

        for r in range(m): # 행
            for c in range(n): # 열로 돌아가면서 dp에 넣기(를 해주고싶었다)
                dp[r][c] = dfs(r,c,[])
        # print(f'dp = {dp}')

        for k in dp: # 각 행에서 최댓값 갱신하며 찾기
            answer = max(answer,max(k))
        return answer 


# 어렵다.... 
# 의식의 흐름대로 풀었던건지 내가 내 코드를 이해못하겠는데;;

# ==========

# 1. 행*열의 이중 for문으로 dp 탐색
# 2. if dp[r][c]가 비어있으면 dfs로 탐색
# 3. def dfs()
# 4. if 방문한적 없는 dp[r][c]라면 방문처리(겸 자기 자신이 최대 길이일 경우의 1 설정)
# 5. 상하좌우 탐색
# 6. 범위를 넘어가지 않고 상하좌우의 수가 본래의 수보다 크다면
# 7. dp에 다시 저장 => dp[r][c]는 본래의 dp 값과 상하좌우 좌표를 다시 dfs 시킨 값(+1) 중 최댓값
# 8. 탐색이 모두 끝났다면 dp에서 최댓값 찾기 