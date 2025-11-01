"""
Gold4
준표의 조약돌
문제 링크 : https://www.acmicpc.net/problem/15831
"""

import sys
input = sys.stdin.readline

def solve():
    n, b, w = map(int, input().split())
    stones = input().rstrip()

    left = 0
    black_count = 0
    white_count = 0
    max_length = 0

    for right in range(n):
        # 현재 돌 추가
        if stones[right] == 'B':
            black_count += 1
        else:
            white_count += 1

        # 검은 조약돌이 b개를 초과하면 left 이동
        while black_count > b:
            if stones[left] == 'B':
                black_count -= 1
            else:
                white_count -= 1
            left += 1

        # 흰 조약돌이 w개 이상이면 최대 길이 갱신
        if white_count >= w:
            max_length = max(max_length, right - left + 1)

    print(max_length)

solve()