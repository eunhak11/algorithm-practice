"""
Silver4
카드 2
문제 링크 : https://www.acmicpc.net/problem/2164
블로그 링크 :
"""

from collections import deque

n = int(input())
dq = deque(range(1, n+1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])
