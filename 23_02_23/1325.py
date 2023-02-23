'''
A가 B를 신뢰하는 경우 B해킹하면 A도가능
A B
가장 많은 해킹 컴퓨터 번호

그래프 만든다음 5,4그래프 앞이 a,b 해당하는 좌표에 1을 넣음
행에 1이 있는걸 찾고 
1,3에 1이 있음 3행을 돌려서 1있는거 찾고 1있는 열을 행으로 바꿔서 찾음

그래프 만들고 그거.....................................?
시작점을 잘 찾아야 한다.
'''
import sys
input = sys.stdin.readline

def dfs(x):
    stack = []
    visited = [False] * (N+1)
    stack.append(x)
    visited[x] = True

    # dfs
    while stack:
        value = stack.pop()
        llst[x] += 1

        length = len(lst[value])
        for j in range(length):
            if not visited[lst[value][j]]:
                stack.append(lst[value][j])
                visited[lst[value][j]] = True

N, M = map(int,input().split())
lst = [list() for _ in range(N+1)]
visited = [0]*(N+1)

for _  in range(M):
    a,b = map(int,input().split())
    lst[b].append(a)
llst = [0] * (N+1)
for i in range(1,N+1):
    dfs(i)
        
a = max(llst)
for j in range(len(llst)):
    if llst[j] == a:
        print(j, end= " ")



