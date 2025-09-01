"""
Silver3
파도반 수열
문제 링크 : https://www.acmicpc.net/problem/9461
블로그 링크 :
"""

import sys

T = int(sys.stdin.readline().strip()) # 테스트케이스

nums = [1, 1, 1]

for i in range(3, 100):
    nums.append(nums[i-2] + nums[i-3])

for _ in range(T):
    N = int(sys.stdin.readline().strip())

    print(nums[N-1])