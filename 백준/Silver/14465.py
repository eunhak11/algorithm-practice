"""
Silver2
소가 길을 건너간 이유 5
문제 링크 : https://www.acmicpc.net/problem/14465
"""

import sys
input = sys.stdin.readline

def solve():
    n, k, b = map(int, input().split())

    # 고장난 신호등 표시
    broken = [False] * (n + 1)
    for _ in range(b):
        num = int(input())
        broken[num] = True

    # 초기 윈도우 (1 ~ k) 고장난 개수 세기
    broken_count = sum(1 for i in range(1, k + 1) if broken[i])
    min_repair = broken_count

    # 슬라이딩 윈도우
    for i in range(k + 1, n + 1):
        # 오른쪽 끝 추가
        if broken[i]:
            broken_count += 1
        # 왼쪽 끝 제거
        if broken[i - k]:
            broken_count -= 1

        min_repair = min(min_repair, broken_count)

    print(min_repair)

solve()
