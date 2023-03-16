# https://www.acmicpc.net/problem/1937
# 욕심쟁이 판다

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cr, cc):
    if dp[cr][cc]:
        return dp[cr][cc]

    dp[cr][cc] = 1
    for d in range(4):
        nr, nc = cr + dx[d], cc + dy[d]
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] > arr[cr][cc]:
            dp[cr][cc] = max(dp[cr][cc], dfs(nr, nc) + 1)
    return dp[cr][cc]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dp = [[0]*n for _ in range(n)]

res = 0
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i, j))
print(res)