# https://www.acmicpc.net/problem/1043
# 거짓말
'''
파티마다 지민이가 할 이야기를 알 수 있는 사람이 있을 수 있다.
과장된 이야기를 할껀데 거짓말쟁이로 낙인 찍힐 수 있는 곳에선 피하려한다.
과장된 이야기를 할 수 있는 파티는 몇개인가

진실을 알고있는 그룹이 주어지고,
그 그룹에 사람이 포함되어있는 파티라면 파티 인원 모두 그룹에 포함된다.

# ㄷㅁ
1. 진실팸 만들기
2. 파티 돌면서 진실팸 모집
3. 마지막에 파티에 진실팸 없으면 cnt 증가

# ㅇㅈ
유니온 파인드?
'''
N, M = map(int, input().split())
tNum, *tPeople = map(int, input().split())
tPeople = set(tPeople)
party = []
for _ in range(M):
    _, *temp = map(int, input().split())
    party.append(set(temp))

if tNum:
    for _ in range(M):
        for i in range(M):
            if tPeople & party[i]:
                tPeople |= party[i]
    cnt = 0
    for i in range(M):
        if not (tPeople & party[i]):
            cnt += 1
    print(cnt)
else:
    print(M)