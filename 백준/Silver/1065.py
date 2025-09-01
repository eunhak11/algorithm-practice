"""
Silver4
다리 놓기
문제 링크 : https://www.acmicpc.net/problem/1065
블로그 링크 :
"""

import sys
input = sys.stdin.readline
n = int(input().rstrip())

if n<100:
    cnt = n
else:
    cnt = 99
    for i in range(100, n+1):
        # 각 자릿수 분리
        hundreds = i // 100      # 백의 자리
        tens = (i % 100) // 10   # 십의 자리
        ones = i % 10            # 일의 자리
        if hundreds-tens == tens-ones:
            cnt+=1
print(cnt)
