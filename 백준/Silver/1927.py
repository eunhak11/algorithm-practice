"""
Silver2
최소 힙
문제 링크 : https://www.acmicpc.net/problem/1972
"""

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, x)