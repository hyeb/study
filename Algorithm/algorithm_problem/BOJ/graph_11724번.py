# 백준 11724번 연결 요소의 개수
# https://www.acmicpc.net/problem/11724


import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

count = 0
for i in range(1, N+1):
    if visited[i] == False: 
        dfs(i)
        count += 1
print(count)


        
# dfs 까지는 어렵지 않게 구현이 가능했지만 (당연함 방금전에 같은 유형 문제 풀어봤음)
# 연결된 노드 구분을 어떻게 할지 물음표였다.
# 노드들을 돌면서 방문하지 않았으면 dfs해주고 빠져나오면 count해주는 방식으로 풀기



## +) 또 다시 찾아온 런타임에러... 한번에 넘어가는 법이 없어~
## 파이썬은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러를 일으킨다고한다.
## 그렇기 때문에 sys.setrecursionlimit(10000)을 해주어야함

## +) 으악 이번엔 시간초과!!!
## 와.. input()때문에 시간초과 나는거였다...


# 프로그래머스의 '네트워크' 문제와 비슷하다고 한다. 