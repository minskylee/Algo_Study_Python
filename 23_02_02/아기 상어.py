'''
bfs네요
물고기 위치, 자기 크기 기록
map 물고기 위치, 자기위치 복사하면서 bfs.....
'''

from collections import deque

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

babysh = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            babysh = [i,j,2,0,0] #위치,상어크기,먹은갯수,시간변수

dc = [0,-1,0,1] #x축
dr = [-1,0,1,0] #상좌하우 y축

def bfs(babysh):
    while True:
        visited = [[0]*N for _ in range(N)]
        que = deque([[babysh[0],babysh[1]]])
        time = 1e9
        visited[babysh[0]][babysh[1]] = 1
        
        while que:
            cr, cc =  que.popleft()
            for k in range(4):
                nr = cr + dr[k] #r이 행 세로
                nc = cc + dc[k] #c이 열 가로
    # 한번먹을때마다 visited판을 갱신
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] <= babysh[2] :
                    visited[nr][nc] = visited[cr][cc] + 1
                    if 0 < arr[nr][nc] < babysh[2] and visited[nr][nc] < time:
                        time = visited[nr][nc]
                    que.append([nr,nc])
        
        if time == 1e9 :
            return babysh[4]
        tmp = 0
        for i  in range(N):
            for j in range(N):
                if babysh[2] > arr[i][j] > 0 and visited[i][j] == time:
                    babysh[3] += 1
                    tmp = 1
                    if babysh[3] == babysh[2]:
                        babysh[2] += 1
                        babysh[3] = 0
                    arr[babysh[0]][babysh[1]] = 0
                    arr[i][j] = 9
                    babysh = [i,j,babysh[2], babysh[3], babysh[4] + time - 1]
                    break
            if tmp == 1:
                break
print(bfs(babysh))

