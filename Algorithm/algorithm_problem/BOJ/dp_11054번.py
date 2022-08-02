# 백준 11054번 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054

# 내가 푼거
N = int(input())
A = list(map(int, input().split()))

d = [1] * N
increase = [1] * N
decrease = [1] * N

for i in range(N): # S(i)를 기준으로
    for j in range(i): # 정방향 탐색 (가장 긴 증가하는 부분 수열)
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)
for i in range(N-1,-1,-1):
    for k in range(N-1,i,-1): # 역방향 탐색 (가장 긴 감소하는 부분 수열)
        if A[i] > A[k]:
            decrease[i] = max(decrease[i], decrease[k]+1)

for i in range(N):
    d[i] = increase[i] + decrease[i] - 1 
print(max(d))



# 기본 아이디어도 조금 어긋나고 중간에 for문 설정하는 방법이 틀림
# 왼쪽, 오른쪽으로 탐색구간을 나누는 것이 아니라 
# 정방향으로 한번 탐색, 그리고 역방향으로도 한번 탐색해줘서 + 해줘야함

# +) 감소하는 수열 찾을 때, 전체 for문(i가 있는)도 역방향으로 시작해야하는데 
# 1->N의 for문에서 부분 for문(2중)으로 증가, 감소를 나눠서 작성했기 때문에 틀림..


# ==============================================================
# 다른 방법

N = int(input())
A = list(map(int, input().split()))
reverse_A = A[::-1] # 역방향 탐색을 위함

d = [1] * N
increase = [1] * N
decrease = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_A[i] > reverse_A[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

for i in range(N):
    d[i] = increase[i] + decrease[N-i-1] - 1
    # decrease 슬라이싱해줄때 주의

print(max(d))

# 가독성이 훨씬 좋은것 같당...
# 참고
# https://seohyun0120.tistory.com/entry/%EB%B0%B1%EC%A4%80-11054-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B0%94%EC%9D%B4%ED%86%A0%EB%8B%89-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4