# 백준 11054번 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054

N = int(input())
A = list(map(int, input().split()))

d = [1] * N
flag = False

for i in range(N): # S(i)를 기준으로
    for j in range(i): # 왼쪽 탐색
        if A[i] > A[j]:
            d[i] = max(d[i], d[j]+1)
    for k in range(i+1,N): # 오른쪽 탐색
        if A[k] > A[i]:
            d[i] = max(d[i], d[k+1])

print(f'd={d}')
print(max(d))