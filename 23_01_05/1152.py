# https://www.acmicpc.net/problem/1152
# 단어의 갯수
'''
input().split() -> 공백 -> 카운트

반복문 -> 공백을 찾는다 -> 카운트

split()
'''
word = list(input().split())
print(len(word))
