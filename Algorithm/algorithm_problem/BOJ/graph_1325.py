# 1325 효율적인 해킹
'''
Q. 딕셔너리가 리스트보다 메모리 효율성이 떨어지는가?
딕셔너리가 리스트보다 속도 측면에서는 더 효율적이라고 알고있는데 메모리 측면에서는 다른건가?
개수가 커지면 메모리 측면에서도 마찬가지일것같은데 참고한 블로그에서 딕셔너리 사용보다 이중 리스트 사용시 메모리 효율성이 더 좋게 나왔다고함.
왜일까..?
'''
from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(n):
    q = deque([n])
    cnt = 0
    visited = [0] * (N+1)
    visited[n] = 1
    while q:
        node = q.popleft()
        cnt += 1
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
    return cnt

answer = [0 for _ in range(N+1)]
for i in range(1, N+1):
    answer[i] = bfs(i)

max_num = max(answer)
for i in range(1, N+1):
    if answer[i] == max_num:
        print(i, end=" ")