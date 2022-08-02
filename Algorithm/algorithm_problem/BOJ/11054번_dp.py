# 백준 11054번 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054

N = int(input())
A = list(map(int, input().split()))

d = [1] * N
increase = [1] * N
decrease = [1] * N

for i in range(N): # S(i)를 기준으로
    print(f'{i}_result')
    for j in range(i): # 정방향 탐색 (가장 긴 증가하는 부분 수열)
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)
    for k in range(N-1,i,-1): # 오른쪽 탐색 (가장 긴 감소하는 부분 수열)
        if A[i] > A[k]:
            decrease[i] = max(decrease[i], decrease[k]+1)

    print(f'increase={increase}')
    print(f'decrease={decrease}')
    d[i] = increase[i] + decrease[i]

print('=====DONE=====')
print(f'd={d}')
print(max(d))

# 기본 아이디어도 조금 어긋나고 중간에 for문 설정하는 방법이 틀림
# 왼쪽, 오른쪽으로 탐색구간을 나누는 것이 아니라 
# 정방향으로 한번 탐색, 그리고 역방향으로도 한번 탐색해줘서 + 해줘야함