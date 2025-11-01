"""
Silver1
스티커
문제 링크 : https://www.acmicpc.net/problem/9465
"""

import sys
input=sys.stdin.readline

def max_sticker_points(n):
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        return max(stickers[0][0], stickers[1][0])

    dp_max = [[0] * n for _ in range(2)]

    dp_max[0][0] = stickers[0][0]
    dp_max[1][0] = stickers[1][0]
    dp_max[0][1] = dp_max[1][0] + stickers[0][1]
    dp_max[1][1] = dp_max[0][0] + stickers[1][1]

    # DP 계산: 세 번째 열부터
    for i in range(2, n):
        dp_max[0][i] = max(dp_max[1][i-1], dp_max[1][i-2]) + stickers[0][i]
        dp_max[1][i] = max(dp_max[0][i-1], dp_max[0][i-2]) + stickers[1][i]

    return max(dp_max[0][n-1], dp_max[1][n-1])

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    print(max_sticker_points(n))


