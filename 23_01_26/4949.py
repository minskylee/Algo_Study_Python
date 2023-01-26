# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상
'''
스택을 사용한다.
'(' 또는 '[' 가 나오면 스택에 넣는다
')' 또는 ']' 가 나오면 스택 마지막 뇨석이랑 비교 확인한다.
같으면 빼고 다르면 No를 출력한다.
'.'까지 아무 이상이 없고, 스택에 아무것도 없으면 Yes를 출력
'''
while True:
    st = input()
    if st == '.':
        break
    stack = []
    for s in st:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(':
                print('no')
                break
            stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[':
                print('no')
                break
            stack.pop()
    else:
        if stack:
            print('no')
        else:
            print('yes')