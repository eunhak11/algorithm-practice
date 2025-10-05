"""
Gold 5
수 고르기
문제 링크 : https://www.acmicpc.net/problem/2230
"""

import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    num = [0 for _ in range(n)]
    for i in range(n):
        num[i] = int(input().rstrip())

    list.sort(num)
    left, right = 0, 1
    answer = sys.maxsize

    while right < n:
        dif = num[right] - num[left]
        if dif < m:
            right += 1
        else:
            answer = min(answer, dif)
            left += 1
            if left == right:
                right += 1

    print(answer)

solve()