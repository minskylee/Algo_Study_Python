# https://www.acmicpc.net/problem/3079
# 입국심사

'''
이분탐색을 어떻게 쓰죠?
매개변수 = 총 시간?
이분탐색 => 0초 ~ time[-1] * M

7배수, 10배수

왼쪽 오른쪽으로 7, 10 잡고 값을 더해줌?
7 10
10 14
14 20
'''
# time 초기값은 어떻게 설정할 것인가?
# time 어떻게 최신화 할것인가
# s, e에는 무슨값을 넣아햐 하는가!

# lower => 원하는값에서 같은게 있으면 같은것 중에 가장 작은값 없으면 원하는값 보다 큰 가장 작은값
# upper => 원하는값보다 큰 가장 작은값

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
s, e = 0, M * arr[0]
while s != e:
    mid = (s + e) >> 1
    f_cnt = 0
    for i in range(N):
        f_cnt += mid // arr[i]
    if f_cnt >= M:
        e = mid
    else:
        s = mid + 1
print(s)
