# https://www.acmicpc.net/problem/1167
# 트리의 지름
'''
# ㄷㅁ
일단 트리를 만들어


# ㅇㅈ
depth가 가장깊은것의 끝과 끝

'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    visited = [0]*(V + 1)
    q.append(1)
    visited[1] = -1
    max_val = 0
    max_idx = 0
    while q:
        s = q.popleft()
        for i, d in adj[s]:
            if not visited[i]:
                visited[i] = visited[s] + d
                if max_val < visited[i]:
                    max_val = visited[i]
                    max_idx = i
                q.append(i)
    
    q = deque()
    visited = [0]*(V + 1)
    q.append(max_idx)
    visited[max_idx] = -1
    while q:
        s = q.popleft()
        for i, d in adj[s]:
            if not visited[i]:
                visited[i] = visited[s] + d
                q.append(i)
    print(max(visited) + 1)

V = int(input())
adj = [[] for _ in range(V + 1)]
leafNode = []
for _ in range(V):
    temp = list(map(int, input().split()))
    if len(temp) == 4:
        leafNode.append(temp[0])
    for i in range(1, len(temp) - 1, 2):
        adj[temp[0]].append((temp[i], temp[i + 1]))

bfs()