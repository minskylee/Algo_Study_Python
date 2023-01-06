# https://www.acmicpc.net/problem/2742
# 기찍 N
'''
print를 사용해서 한번에 찍는다
sep=''
end=''
'''
n = int(input())
lst = [n-i for i in range(n)]
print(*lst, sep='\n')
