# 백준 11055번 가장 큰 증가 부분 수열
# https://www.acmicpc.net/problem/11055

# 이전의 11053번 가장 긴 증가하는 부분 수열 문제와 비슷

N = int(input())
A = list(map(int, input().split()))

# dp = [A[0]] * N   / 처음에 이렇게 했는데 계속 틀려버려서
dp = [1] * N
dp[0] = A[0] # 이렇게 바꾸었더니 맞음... 근데 중간 계산에 어떤 영향을 미쳐서 다른건지는 모르겠음

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]: # i에 해당하는 수가 크다면
            dp[i] = max(dp[i], dp[j]+A[i]) # dp[i]는 A[i]까지의 증가 부분 수열 합
        else: # 작다면
            dp[i] = max(A[i], dp[i]) # 지금까지의 합이나 자기 자신 중 큰 값을 넣어주기
            
# print(f'dp: {dp}')
print(max(dp))

# i에 해당하는 수보다 작은 경우도 고려해주어야 했음
