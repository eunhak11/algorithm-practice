"""
Silver2
과자 나눠주기
문제 링크 : https://www.acmicpc.net/problem/16401
"""

import sys
input = sys.stdin.readline

def can_distribute(length, snacks, m):
    if length == 0:
        return True

    count = 0
    for snack in snacks:
        count += snack // length
        if count >= m:
            return True
    return False

def solve():
    m, n = map(int, input().split())
    snacks = list(map(int, input().split()))

    if sum(snacks) < m:
        print(0)
        return

    left, right = 1, max(snacks)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_distribute(mid, snacks, m):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)

solve()