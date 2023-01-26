# https://www.acmicpc.net/problem/7569
# 토마토
'''
Bfs로 구현
'''
from collections import deque

def bfs():
    queue = deque(Etomato)
    max_day = 0
    while queue:
        ch, cr, cc = queue.popleft()
        for d in dd:
            nh, nr, nc = ch+d[0], cr+d[1], cc+d[2]
            if 0 <= nr < N and 0 <= nc < M and 0 <= nh < H and not arr[nh][nr][nc] and not visited[nh][nr][nc]:
                arr[nh][nr][nc] = 1
                visited[nh][nr][nc] = visited[ch][cr][cc] + 1
                max_day = max(max_day, visited[ch][cr][cc])
                queue.append((nh, nr, nc))
    
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if not arr[k][i][j]:
                    return -1
    return max_day


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dd = [[0, 1, 0], [1, 0, 0], [0, -1, 0], [-1, 0, 0], [0, 0, -1], [0, 0, 1]]

Etomato = []
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                Etomato.append((k, i, j))
                visited[k][i][j] = 1

print(bfs())