# 백준 10844번 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

# 점화식: 
# j=0, dp[i][j] = dp[i-1][j]
# j=9, dp[i][j] = dp[i-1][8]
# j=2~8, dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

n = int(input())
dp = [[0] * 10 for _ in range(101)]

for k in range(1,10):   # 한 자리수일 땐 다 1이기 때문에
    dp[1][k] = 1

for i in range(2, n+1): # 두 자리수일때부터 고려하기
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] # 0은 1과 함께일 경우밖에 없음
        elif j == 9:
            dp[i][j] = dp[i-1][8] # 9는 8과
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)



## 이번거.. 2차원으로 생각해야해서 좀..... 
## 점화식 찾는거ㅜㅜ