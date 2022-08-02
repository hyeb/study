# 백준 15649번 N과 M (1)
# https://www.acmicpc.net/problem/15649

# 백트래킹 문제

N, M = map(int, input().split())
stack = []
visited = [0] * (N+1)

def dfs():
    if len(stack) == M:
        print(' '.join(map(str,stack)))
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        stack.append(i)
        dfs()
        stack.pop()
        visited[i] = 0

dfs()


## 이분 풀이법으로 이해함
## https://velog.io/@yusuk6185/%EB%B0%B1%EC%A4%80-15649-N%EA%B3%BC-M-1-%ED%8C%8C%EC%9D%B4%EC%8D%AC-with-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9

