# 백준 1260번 DFS와 BFS
# https://www.acmicpc.net/problem/1260

# 으악 그래프 문제!
# 양방향 그래프!!!
from collections import deque

N, M, V = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(M)]
graph = {}
for _ in range(M):
    k, v = map(int, input().split())
    if k in graph:
        graph[k].append(v)
    else:
        graph[k] = [v]

print(f'graph = {graph}')

visited = [False] * (N+1)
stack = []

def dfs(graph, visited, node, res):
    visited[node] = True # 방문체크
    if node not in res:
        res.append(node)
        print(f'node={node} res={res}')
    if node in graph:
        for n in sorted(graph[node]):
            dfs(graph, visited, n, res)
    return res

print(dfs(graph, visited, V, []))
# 이거 두 번째 테스트 케이스는 안됨.. 딕셔너리에 저장한 방법이 양방향이 아니기 때무네..ㅜ

# def bfs():
# bfs 는 손도 못댔음ㅎ

