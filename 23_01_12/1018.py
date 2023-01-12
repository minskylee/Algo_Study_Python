'''
1.
for i in range(m-8) 전체 탐색
for j 해서 0부터 n-8까지
for a 8:
    for b 8:
        최소인 부분 찾아서 업데이트

2.
매트리스 미리 만들어 놓고 비교해서 값이 다른거 찾고, 젤 작은 곳

3.
좌표값을 더했을 때 짝수냐 홀수냐에 따라
'''

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
# print(*arr,sep='\n')
min_cnt = 64

for i in range(N-8+1):
    for j in range(M-8+1):
        # print(arr[i][j])
        cnt1=cnt2=0
        for r in range(8):
            for c in range(8):
                if (i+r+j+c) % 2 == 0:
                    if arr[i+r][j+c] == 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if arr[i+r][j+c] == 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        min_cnt = min(min_cnt,min(cnt1,cnt2))
print(min_cnt)