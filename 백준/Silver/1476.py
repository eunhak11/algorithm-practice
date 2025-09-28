"""
Silver5
날짜 계산
문제 링크 : https://www.acmicpc.net/problem/1476
"""
import sys

e, s, m = map(int, sys.stdin.readline().split())

date = [1, 1, 1]
idx = 1

while 1:
    if date[0]==e and date[1]==s and date[2]==m:
        print(idx)
        break

    date[0] += 1
    date[1] += 1
    date[2] += 1

    date[0] = 1 if date[0] > 15 else date[0]
    date[1] = 1 if date[1] > 28 else date[1]
    date[2] = 1 if date[2] > 19 else date[2]

    idx += 1