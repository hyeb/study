# 백준 10451번 순열 사이클
# https://www.acmicpc.net/problem/10451

def cycle_check(visited, num, start, count):
    visited[num] = True
    count += 1
    # 이미 방문한 상태고 처음 시작 숫자와 같다면 사이클 완성이므로 반환
    if visited[num-1] == True and visited[num] == start:
        return count

    if False not in visited: # 모두 한번씩 방문해봤다면 빠져나오기
        return
    
    cycle_check(visited, num) # 아니라면 계속 체크하기

T = int(input())

for _ in range(T):
    N = int(input())
    array = list(map(int, input().split()))
    res = 0
    visited = [False] * (len(array)+1)
    visited[0] = True
    for i in range(len(array)):
        count = 0
        start = i+1
        visited[i+1] = True
        res += cycle_check(visited, array[i], start, count)

    print(res)
