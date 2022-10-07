# Baekjoon 1697번 숨바꼭질
# https://www.acmicpc.net/problem/1697

# bfs로 풀이

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 10**5
dist = [0] * (MAX+1)

q = deque([N])
while q:
    num = q.popleft()
    if num == K:
        print(dist[num])
        break
    
    for i in [num-1, num+1, num*2]:
        if 0 <= i <= MAX and not dist[i]:
            dist[i] = dist[num] + 1
            q.append(i)