'''
21 ~ 26 번째줄의 순서 때문에 계속 틀림 (처음에 while문과 if문 위치가 반대였음)
- melody[m] -> m번째 줄에 원소가 있다는 것은 이미 해당 줄을 누르고 있다는 것
- 그렇다면 해당 줄의 가장 높은 음과 입력받은 p를 비교해주어야 함

처음에는 높은 음이 p와 같으면 손가락을 움직일 필요가 없으니까 순서가 상관없을거라고 생각했었는데
melody[m][-1] > p 경우 
- 빈 리스트가 되는 경우
- p가 높은 음이 되거나 같아질 경우
두 가지 경우가 될때까지 while이 반복될텐데 원래 내 순서대로하면 두 번째 경우 p가 같아졌을때 문제가 발생함
같아졌을때를 처리하는 로직이 없으니 이미 p를 누르고 있는데 또 리스트에 넣어주게 되니까... 이 부분을 생각 못했었다
'''
import sys
input = sys.stdin.readline
N, P = map(int, input().split())
melody = [[] for _ in range(7)]
ans = 0
for _ in range(N):
    m, p = map(int, input().split())

    while melody[m] and melody[m][-1] > p:
        melody[m].pop()
        ans += 1
    
    if melody[m] and melody[m][-1] == p:
        continue
    
    melody[m].append(p)
    ans += 1
    
print(ans)