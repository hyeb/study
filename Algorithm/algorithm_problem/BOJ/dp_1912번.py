# 백준 1912번 연속합
# https://www.acmicpc.net/problem/1912


n = int(input())
array = list(map(int, input().split()))

d = [0] * n
d[0] = array[0]

for i in range(1, n):
    d[i] = max(array[i], d[i-1] + array[i])
print(max(d))