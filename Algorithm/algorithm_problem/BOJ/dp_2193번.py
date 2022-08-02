# 백준 2193번 이친수
# https://www.acmicpc.net/problem/2193

# 점화식: d[n] = d[n-1] + d[n-2]

n = int(input())
d = [0] * 91
d[1], d[2] = 1, 1

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

# 으악 점화식!!!!!!!