# https://www.acmicpc.net/problem/14267
# 회사 문화 1

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def set_score(people, pre_score):
    score[people - 1] += pre_score
    for i in tree[people]:
        set_score(i, score[people - 1])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
score = [0]*n
for i in range(1, n):
    tree[arr[i]].append(i + 1)
for _ in range(m):
    i, w = map(int, input().split())
    score[i - 1] += w
set_score(1, 0)
print(*score)
