# 백준 1074번 Z
# https://www.acmicpc.net/problem/1074

# 4 등분 후 z 방향으로 배열을 방문하는 것 생각하기
# 반복되는 부분이 있으니 재귀 사용하기
# 찾아야하는 좌표가 주어지기 때문에 어느 사분면에 있는지 계산하면서 찾아가기

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
count = 0

def search(x,y,n):
    global count
    if x==r and y==c:
        print(ans)
        exit(0)
    if n==1:
        ans += 1
        return
    if not (x<=r<x+n and y<=c<y+n):
        ans += n*n
        return
    temp = n//2
    search(x,y,temp)
    search(x,y+temp, temp)
    search(x+temp, y, temp)
    search(x+temp, y+temp, temp)


# 짧고 굵게... 이렇게 푸는 방법도 있었다..

def sol(N,r,c):
    if N == 0:
        return 0
    return 2*(r%2)+(c%2) + 4*sol(N-1,int(r/2),int(c/2))

# 2*(r%2)+(c%2) => 화살표
# 4*sol(N-1,int(r/2),int(c/2)) => 4의 배수하기 이전의 값