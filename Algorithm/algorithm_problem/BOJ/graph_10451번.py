# 백준 10451번 순열 사이클
# https://www.acmicpc.net/problem/10451

import sys
sys.setrecursionlimit(10**7)

def cycle_check(num):
    visited[num] = True
    next = array[num]
    if visited[next] == False:
        cycle_check(next)

T = int(input())

for _ in range(T):
    N = int(input())
    array = [0] + list(map(int, input().split()))
    res = 0
    visited = [False] * (N+1)

    for i in range(1, N+1):
        if visited[i] == False:
            cycle_check(i) 
            res += 1 # 빠져나오면 그게 1 사이클이기 때문에 +1

    print(res)


# N이 주어졌는데 왜 len으로 하고있었지 ㅋㅋㅋ
# 초반의 기본 아이디어는 잘 떠올렸지만 중간에 생각이 조금 꼬인듯하다

## 런타임에러가 났다.. 제한리밋 풀어줘야함