# https://www.acmicpc.net/problem/7662
# 이중 우선순위 큐
'''
해쉬에 데이터가 들어가고 나가고 기록
힙을 2개만들어서
하나는 최소힙, 하는 최대힙
데이터 삭제 삽입을 할껀데

1 2 3 4 5 -> IN
hash : 1 = 0, 2 = 0, 3 = 0 ... 5 = 0, 6 = 1

5 -> Out
6 -> In

최대힙 : 6 4 3 2 1
최소힙 : 6
'''
import sys
import heapq
input = sys.stdin.readline

def inheap(num):
    if num not in db:
        db[num] = 1
    else:
        db[num] += 1
    heapq.heappush(min_heap, num)
    heapq.heappush(max_heap, (-num, num))

def outheap(flg):
    if flg == -1:
        if min_heap:
            if db[min_heap[0]] <= 0:
                while min_heap and db[min_heap[0]] <= 0:
                    heapq.heappop(min_heap)
                    if not min_heap:
                        return
            num = heapq.heappop(min_heap)
            db[num] -= 1
    else:
        if max_heap:
            if db[max_heap[0][1]] <= 0:
                while max_heap and db[max_heap[0][1]] <= 0:
                    heapq.heappop(max_heap)
                    if not max_heap:
                        return
            num = heapq.heappop(max_heap)[1]
            db[num] -= 1

T = int(input())
for tc in range(1, T+1):
    k = int(input())
    db = dict()
    min_heap = []
    max_heap = []
    for _ in range(k):
        command, num = input().split()
        num = int(num)
        if command == 'I':
            inheap(num)
        else:
            outheap(num)
    lst = []
    for key, value in db.items():
        if value:
            lst.append(key)
    lst.sort()
    if not lst:
        print('EMPTY')
    else:
        print(lst[-1], lst[0])


