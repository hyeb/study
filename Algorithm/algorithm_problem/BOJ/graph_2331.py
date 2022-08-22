# 백준 2331번 반복수열
# https://www.acmicpc.net/problem/2331

A, P = map(int, input().split())

array = [A]

while True:
    num = 0
    for i in str(array[-1]):
        num += int(i) ** P
    
    if num in array:
        break
    array.append(num)

print(array.index(num))

# 문제 이해하는데 시간이 좀 걸렸는데 로직 자체는 간단한것같다
# 수열의 길이 출력하는 부분을 어떻게해야할지 물음표였는데 간단하게 해결 가능한거였다,,

# 계속해서 배열에 숫자를 추가해가면서 반복되는지 확인하고
# 반복된다면 빠져나와서 해당하는 인덱스 출력
# 아니라면 계속 반복

# 참고
# https://leeiopd.tistory.com/entry/BOJ-2331-%EB%B0%98%EB%B3%B5%EC%88%98%EC%97%B4-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC