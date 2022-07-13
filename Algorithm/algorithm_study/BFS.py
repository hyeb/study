# BFS basic code
from collections import deque

def BFS(graph, node, visited):
    queue = deque([node])
    visited[node] = 1 # 방문 체크

    while queue: # 큐가 빌 때까지
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]: # 방문하지 않은 노드가 있다면
                visited[i] = 1
                queue.append(i)