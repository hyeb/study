# 백준 2579번 계단 오르기
# https://www.acmicpc.net/problem/2579

# 포도주 문제랑 비슷한것 같다. 다만, 이 문제는 마지막 계단이 반드시 포함되어야 함! 
# 그럼 마지막 계단이 이미 밟혀있다는 것을 전제로 계산하기


N = int(input())
stairs = [int(input()) for _ in range(N)]

dp = [0] * N

if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[1]+stairs[0]
    dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])

    for i in range(3, N):
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])
    print(dp[N-1])

## +) N이 1,2 일 케이스를 따로 고려해주지않아서 여러번 틀림..
## +) 마지막에 max(dp)가 아니라 마지막 계단 즉, max(dp[N-1])로 고려해줘야 한다는 부분에서도..