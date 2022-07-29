# 백준 9465번 스티커
# https://www.acmicpc.net/problem/9465

# 스티커 하나를 선택하면 [위, 아래, 왼쪽, 오른쪽]으로 인접해있는 스티커는 뗄 수 없다.
# == 현재 스티커의 최댓값은 대각선 방향의 [n-1]과 [n-2]의 값중 최대값을 더해주기

#=======================<< 내가한거 >>========================

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    
    dp[0][1] += dp[1][0] # 대각선 방향의 수를 더해주는 방식
    dp[1][1] += dp[0][0] # 시작 루트는 두 가지 뿐이기 때문에

    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    
print(max(dp[0][n-1], dp[1][n-1]))


## ... 왜 자꾸 런타임 에러가 나는거지??? 왜????? 이거 진짜 맞왜틀
## 10번이나 시도했는데 하...



#=======================<< 다른 분 코드 참고 >>========================

T = int(input())

for _ in range(T):
    n = int(input())
    dp = []
    for _ in range(2):
        dp.append(list(map(int, input().split())))
    
    for i in range(1,n):
        if i == 1:
            dp[0][i] += dp[1][i-1]
            dp[1][i] += dp[0][i-1]
        else:
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])

print(max(dp[0][n-1], dp[1][n-1]))


# 참고(라 쓰고 ctrl+c라 읽음)
# https://pacific-ocean.tistory.com/197


## ... 내 코드랑 어느 부분에서 차이나는지 모르겠음..ㅜㅜ