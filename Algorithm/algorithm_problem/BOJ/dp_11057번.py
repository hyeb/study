# 백준 11057번 오르막 수
# https://www.acmicpc.net/problem/11057

# 점화식: d[n] += d[i] for i in range(n+1)

n = int(input())
dp = [[0] * 10 for _ in range(1001)]

for k in range(10):
    dp[1][k] = 1

for i in range(2, n+1):
    for j in range(10):
        for m in range(j+1):
            dp[i][j] += dp[i-1][m]

print(sum(dp[n]) % 10007)

# 숫자를 만드는게 아니기 때문에 앞자리에 0이 와도 되는데 이걸 생각 못하고..