# 백준 1260번 DFS와 BFS
# https://www.acmicpc.net/problem/1260
# 으악 그래프 문제!



# 노드 저장할때 dic 안쓰고 graph[a][b] 이중배열로 저장하는 방법도 있었구나...!ㄴㅇㄱ
# graph[a] = []를 가지도록 만드는 방법도 있는데 이러면 정렬을 따로 해줘야하니까 위의 방법이 더 편할듯
# 와.. 결과를 반환할 리스트를 따로 만들어주는것이 아니라 print할때 end=' '로 그냥 출력해버리는 방버ㅂ....

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
print(f'graph = {graph}')

# 요런 방법도 있음 대신 정렬을 따로 해줘야함
# graph = [[] for _ in range(N+1)]
# for i in range(N):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# =================================================================
from collections import deque

# 내가 푼... code
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


# 이렇게 풀면되는거였음.. 외워야겠다
dfs_visited = [False] * (N+1)
def dfs(v):
    dfs_visited[v] = True
    print(v, end=' ')
    for i in range(1, N+1):
        if dfs_visited[i] == 0 and graph[v][i] == 1:
            dfs(i)
    

# bfs 는 손도 못댔음ㅎ
bfs_visited = [False] * (N+1)
def bfs(v):
    q = deque([v])
    bfs_visited[v] = True
    while q:
        num = q.popleft()
        print(num, end=' ')
        for i in range(1, N+1):
            if bfs_visited[i] == False and graph[num][i] == 1:
                q.append(i)
                bfs_visited[i] = 1

dfs(V)
print()
bfs(V)



## 참고
# https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-1260%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://www.devchopin.com/blog/96/