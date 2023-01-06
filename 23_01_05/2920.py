# https://www.acmicpc.net/problem/2920
# 음계
'''
반복문 -> 0 ~ N까지 빼서 +냐 -냐 판단

끝숫자를 먼저 판단 -> + - 를 판단한 뒤 반복문

---
1~8, 8~1을 제외한 모든 리스트는 mixed

'''
lst = list(map(int, input().split()))
pm = 0
if lst[0] == 8 and lst[-1] == 1:
    pm = -1 # descending
elif lst[0] == 1 and lst[-1] == 8:
    pm = 1  # ascending
else:
    pm = 0  # mixed

for i in range(1, len(lst)):
    if lst[i] - lst[i-1] != pm:
        pm = 0
        break

print('descending' if pm == -1 else 'ascending' if pm == 1 else 'mixed')

'''
lst = list(map(int, input().split()))
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [8, 7, 6, 5, 4, 3, 2, 1]
if lst == a:
    print('ascending')
if lst == b:
    print('descending')
else:
    print('mixed')
'''