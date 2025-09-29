"""
Gold 5
용액
문제 링크 : https://www.acmicpc.net/problem/2467
"""

import sys
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    solutions = list(map(int, input().split()))
    head, tail = 0, len(solutions)-1
    res = [int(sys.maxsize), 0, 0] # 0에 가장 가까운 값, head idx, tail idx

    while head<tail:
        mid = solutions[head] + solutions[tail]
        if abs(mid) <= abs(res[0]):
            res[0] = mid
            res[1], res[2] = solutions[head], solutions[tail]
        if mid<0:
            head +=1
        else:
            tail -= 1

    print(res[1], res[2])

solve()