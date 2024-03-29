# 백준 2156번 포도주 시식
# https://www.acmicpc.net/problem/2156

# 설명
# 연속으로 놓여있는 3잔을 모두 마실 수 없다는 조건이 핵심인듯
# 마지막 잔을 마시지 않을 수도 있다는 점을 고려해야함

# i == 현재 마신잔
# 1) wine[i]+wine[i-1]+dp[i-3]: 현재 잔, 이전 잔, 전전의 잔을 마셨을 경우
# 2) wine[i]+dp[i-2]: 현재 잔, 전전 잔을 마시고 \ 이전 잔은 마시지 않을 경우
# 3) dp[i-1]): 현재 포도주를 마시지 않을 경우
# 현재 포도주를 마실지 말지 결정 할때 위의 3가지 경우를 고려 

# ===============


n = int(input())

wine = [0] * (n+2) # 앞뒤로 0을 붙여주기 위해
for w in range(n):
    wine[w+1] = int(input())

dp = [0] * (n+2)
dp[1] = wine[1] # 1, 2까지는 최대값이 연속으로 마신 경우이기 때문에
dp[2] = dp[1] + wine[2] # 값을 지정해주기

for i in range(3, n+1): # 위의 3가지 경우를 확인해가며 max인값으로 지정해주기
    dp[i] = max(wine[i]+wine[i-1]+dp[i-3], wine[i]+dp[i-2], dp[i-1])

print(dp[n])


# ==================
# dp에 이미 누적값이 들어있으니 현재를 기준으로 현재 잔의 용량과
# 이전의 누적된 값들로 고려
# (wine 리스트와 dp 리스트 사용하는게 헷갈렸기 때문에 적음)