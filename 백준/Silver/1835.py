"""
Silver4
카드
문제 링크 : https://www.acmicpc.net/problem/1835
블로그 링크 :
"""
import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n = int(input())

    if n == 1:
        print(1)
    else:
        deq = deque([n])  # 마지막 카드만 시작

        # n-1부터 1까지 역순으로 처리
        for i in range(n - 1, 0, -1):
            deq.appendleft(i)  # 현재 카드를 맨 앞에 추가
            for _ in range(i):
                deq.appendleft(deq.pop())
        print(*deq)

solve()