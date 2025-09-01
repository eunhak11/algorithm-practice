"""
Silver5
다리 놓기
문제 링크 : https://www.acmicpc.net/problem/1010
블로그 링크 :
"""

import math

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(math.comb(m, n)) #mCn