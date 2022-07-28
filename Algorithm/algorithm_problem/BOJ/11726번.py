# 백준 11726번 2*n 타일링
# https://www.acmicpc.net/problem/11726

# dp는 일단 규칙을 파악해서 점화식 세우는게 중요한것같다. 근데 어려움..

## 점화식 : dp[n] = dp[n-1] + dp[n-2]

n = int(input())
d = [0] * 1001 # n의 최대범위가 1000까지니까 요렇게
d[1], d[2] = 1, 2 # 2*1: 1개 2*2: 2개

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n] % 10007)
