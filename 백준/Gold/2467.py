"""
Gold 5
용액
문제 링크 : https://www.acmicpc.net/problem/2467
"""

import sys
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    liquids = list(map(int, input().split()))
    left, right = 0, len(liquids) - 1

    min_sum = sys.maxsize
    answer_left, answer_right = 0, 0

    while left < right:
        current_sum = liquids[left] + liquids[right]
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            answer_left, answer_right = liquids[left], liquids[right]

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    print(answer_left, answer_right)

solve()