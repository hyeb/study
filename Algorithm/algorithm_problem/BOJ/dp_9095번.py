# 백준 9095번 1,2,3 더하기
# https://www.acmicpc.net/problem/9095

# 점화식: d[n] = d[n-1] + d[n-2] + d[n-3]

# 첫 번째
T = int(input())

def sol(n):
    d = [0] * 11    # n은 양수이고 11보다 작다 라는 조건 참고
    d[1], d[2], d[3] = 1, 2, 4

    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    
    return d[n]

for _ in range(T):
    n = int(input())
    print(sol(n))

# 그치만 런타임 에러가 났음..
# 그것은 sol 함수에서 d 길이를 n으로 해줬기 때문에
# 즉, d = [0] * (n+1) 이 아니라 d = [0] * 11

## 점화식만 잘 찾으면 풀만한듯!!! 물론 이건 쉬운축에 속한 문제일수있지만,,