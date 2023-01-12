'''
w // 2 가 x 보다 크면 x 가 왼쪽에 있다는 것, x 가 크면 x와 w 값을 뺀다
h // 2 가 y 보다 크면 위와 같다. h - y 가 거리가 된다.
최소값 출력

x-0, y-0, w-x, h-y min
'''
x,y,w,h = map(int,input().split())
print(min(x-0, y-0, w-x, h-y))