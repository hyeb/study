# 백준 2579번 계단 오르기
# https://www.acmicpc.net/problem/2579

# 포도주 문제랑 비슷한것 같다. 다만, 이 문제는 마지막 계단이 반드시 포함되어야 함! 
# 그럼 마지막 계단이 이미 밟혀있다는 것을 전제로 계산하기


N = int(input())
stairs = [int(input()) for _ in range(N)]

dp = [0] * N
dp[0] = stairs[0]
dp[1] = max(stairs[1], stairs[1]+stairs[0])
dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])

for i in range(3, N):
    dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])
print(max(dp))