"""
골드 4
타일 채우기
문제 링크 : https://www.acmicpc.net/problem/2133
"""

import sys

n = int(sys.stdin.readline().rstrip())

if n % 2 == 1:
    print(0)
else:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3

    special_sum = dp[0]  # 특수 케이스 누적합

    for i in range(4, n + 1, 2):
        dp[i] = dp[i-2] * 3 + special_sum * 2
        special_sum += dp[i-2]  # 다음을 위해 누적

    print(dp[n])