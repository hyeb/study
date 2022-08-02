# 백준 11053번 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

# hint1: 마지막 오는 숫자를 케이스로 나눠서 푸는 문제
# hint2: dp 리스트에 자신을 포함하여 만들수 있는 부분 수열 크기를 저장해야한다.
# me: 와;

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N # 이미 첫번째 수부터 1이 되기 때문에 1로 지정

for i in range(N): # 현재 수
    for j in range(i): # 현재 수의 이전 수들 비교
        if A[i] > A[j]: # 현재 수가 더 크다면
            dp[i] = max(dp[i], dp[j]+1) # 현재 수의 부분 수열 크기 vs 이전 수의 부분 수열 크기 +1 중 최대값
            # 작으면 초기값인 1로 되어있을테니 상관없음 (여기가 헷갈렸었다)
print(max(dp))