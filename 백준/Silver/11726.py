"""
Silver3
2xn 타일링
문제 링크 : https://www.acmicpc.net/problem/11726
"""

import sys

n = int(sys.stdin.readline().rstrip())

if n == 1:
      print(1)
elif n == 2:
    print(2)
else:
    # DP 초기값
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    # DP 계산
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

    print(dp[n])