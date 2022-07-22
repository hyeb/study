# 백준 7576번 토마토
# https://www.acmicpc.net/problem/7576

import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
TOMATO = [list(map(int, input().split())) for _ in range(N)]

# 좌표를 넣어주기위해 빈 리스트 넣어주기
queue = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

# 처음 익은 토마토 위치 찾기
for i in range(N):
    for j in range(M):
        if TOMATO[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            # 익힐 토마토 찾기
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and TOMATO[nx][ny] == 0:
                TOMATO[nx][ny] = TOMATO[x][y] + 1
                queue.append([nx,ny])
bfs()
for tomato in TOMATO:
    for t in tomato:
        # 토마토를 전부 익히지 못했다면 -1 출력
        if t == 0:
            print(-1)
            exit(0)
    # 다 익혔으면 최댓값
    ans = max(ans, max(tomato))
print(ans-1)



# 참고
# https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8