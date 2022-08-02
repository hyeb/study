# 백준 11722번 가장 긴 감소하는 부분 수열
# https://www.acmicpc.net/problem/11722

N = int(input())
A = list(map(int, input().split()))

d = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] > A[i]:
            d[i] = max(d[i], d[j] + 1)
print(max(d))

## for문의 범위가지고 엄청 삽질했네...