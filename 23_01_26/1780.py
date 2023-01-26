# https://www.acmicpc.net/problem/1780
# 종이의 개수
'''
분할정복
입력을 받아서 첫글자랑 다른거 비교해서 다른게 나오면 분할한다.
반복한다
갯수센다

9획으로 자르고 
'''
import sys
input = sys.stdin.readline

def dfs(N, r, c):
    for i in range(r, r + N):
        for j in range(c, c + N):
            if arr[r][c] != arr[i][j]:
                for k in range(3):
                    for l in range(3):
                        dfs(N//3, r + (N//3)*k, c + (N//3)*l)
                return
    num_cnt[arr[r][c]+1] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

num_cnt = [0]*3

dfs(N, 0, 0)

print(*num_cnt, sep='\n')