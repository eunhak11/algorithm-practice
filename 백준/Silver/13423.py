"""
Silver2
Three Dots
문제 링크 : https://www.acmicpc.net/problem/13423
"""

from collections import defaultdict
import sys

def solve():
    input = sys.stdin.readline
    t = int(input().rstrip())

    for _ in range(t):
        n = int(input())
        dots = sorted(list(map(int, input().split())))

        spot_list = defaultdict(int)
        for i in range(len(dots)):
            spot_list[dots[i]] = 1
        res =0

        for i in range(n-1):
            for j in range(i+1, n):
                first = dots[i]
                second = dots[j]
                third = second + (second -first)
                if spot_list[third] == 1:
                    res += 1
        print(res)

solve()