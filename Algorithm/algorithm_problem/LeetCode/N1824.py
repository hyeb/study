# LeetCode 1824. Minimum Sideway Jumps
# https://leetcode.com/problems/minimum-sideway-jumps/description/

'''
- 다이나믹 프로그래밍
- 로직은 크게 side-jump 있는 경우, side-jump 없는 경우로 나눠서 판단
- 처음은 3차선에서 장애물 여부만 판다하면서 앞으로 가는 경우로 dp에 저장하고
- 그 다음 해당 포인트에서 최소값을 저장
- 다시 3차선에서 장애물 여부를 판단하면서 해당 dp값과 최소값+1한 것중 최소로 다시 저장
- 최소값+1 ==> side-jump하는경우

참고: https://leetcode.com/problems/minimum-sideway-jumps/solutions/1152416/python3-dp-solution/?orderBy=hot
'''

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        INF = 100000 * 5
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = dp[0][2] = 1

        for i in range(1,n):
            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = INF

            point_min = min(dp[i])

            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[i][j] = min(dp[i][j], point_min+1)

        return min(dp[-1])