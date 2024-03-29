# 백준 2133번 타일 채우기
# https://www.acmicpc.net/problem/2133

# 점화식 찾는게 너무 어려웠음... 

# 예) 3*2 -> 3  |   3*4 -> 11
# case1: 끝점으로부터 2칸을 채워야하는 경우 => 3가지 존재 (ㅛ = ㅠ)
# case2: 가로가 N일때만 가능한 경우의 수 => 2가지 (_| -|)
# 솔직히 그림 그려봐야 이해감

# 타일묶음의 가로 길이를 고려해줘야하는 것 같다.

# ----------------------------
# N이 홀수면 0 출력

N = int(input())

dp = [0] * (N+1)
if N > 1:
    dp[2] = 3

    for i in range(4, N+1, 2): # 2칸씩 이동
        dp[i] = dp[i-2] * 3 + 2 + sum(dp[:i-2])*2

print(dp[N])


## +) 거의 막바지에 런타임 에러가 나는데 무슨 문제일까..
## N = 1인 경우 dp[2] = 3에서 index 에러 발생
## 나는 if N > 1: 로 해줬지만 처음 dp범위를 [0]*31로 해결하는 방법도 있음. 


# 참고
# https://hongcoding.tistory.com/84
# https://suri78.tistory.com/103