# https://www.acmicpc.net/problem/1149
# RGB거리
'''
# ㄷㅁ
N만큼 차례대로 입력을 받음
같은색깔이 아니면서 최솟값인 애를 배열에 입력받음

'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])

print(min(arr[N-1]))