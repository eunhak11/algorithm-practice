"""
Silver5
2차원 배열의 합
문제 링크 : https://www.acmicpc.net/problem/2167
"""

import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    # 배열 입력 받기
    arr = [[0] * (m + 1)]
    for _ in range(n):
        row = [0] + list(map(int, input().split()))
        arr.append(row)

    # 2D 누적합 배열 생성
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = arr[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

    # 쿼리 처리
    k = int(input().rstrip())
    for _ in range(k):
        i, j, x, y = map(int, input().split())
        result = prefix[x][y] - prefix[i-1][y] - prefix[x][j-1] + prefix[i-1][j-1]
        print(result)

solve()