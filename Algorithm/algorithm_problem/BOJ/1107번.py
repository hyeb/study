# 백준 1107번 리모컨
# https://www.acmicpc.net/problem/1107

# ---<< 내가 생각한 방식>>---
# N 보다 작고 버튼리스트에 없는 숫자로 만들 수 있는 가장 큰 숫자를 먼저 찾기

## 그러나 브루트포스로 풀 수 있는 문제였다..



import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
buttons = {str(i) for i in range(10)}
if M != 0:
    buttons -= set(input().split()) # 사용가능한 버튼들만 남기기

# 현재 보고있는 채널에서 N까지 +- 버튼을 눌러야 하는 횟수
min_cnt = abs(100-N)

for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if str(num[j]) not in buttons: # 누를 수 없는 버튼이 있으면 넘어가기
            break
        elif j == len(num) - 1: # 다 누룰 수 있는 버튼이라면
            # 기존의 것과 현재 숫자에서 N을 뺀 절대값을 구하고 채널번호에서 N까지 눌러야하는 횟수를 더한 것 중 최소값
            min_cnt = min(min_cnt, abs(i-N) + len(num))
print(min_cnt)






# 생각한걸 구현하려니 이것저것 고려할게 많아지면서 막막해져버려서 검색해서 참고했다.
# 왜 바로 이런 아이디어가 안떠오르는걸까ㅠ