# 백준 1463번. 1로 만들기
# https://www.acmicpc.net/problem/1463
# DP 문제 -> 재귀?

# 앞에서 구한 결과값을 저장해두고 나중에 다시 사용

n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # 2,3으로 나누어 떨어지지않는 경우는 무조건 1을 빼야하기 때문에 +1(횟수니까)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1) # 나누어 떨어질경우 어차피 여기서 값이 바뀜
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[n])