# BOJ 1967. 트리의 지름
# https://www.acmicpc.net/problem/1967


n = int(input())

# 트리구현을 못하겄는데...?
graph = [[] for _ in range(n)]
for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

