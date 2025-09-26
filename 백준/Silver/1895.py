"""
Silver4
필터
문제 링크 : https://www.acmicpc.net/problem/1895
"""

import sys

def solve():
    input = sys.stdin.readline

    R, C = map(int, input().split())
    matrix = []
    for i in range(R):
        row = list(map(int, input().split()))
        matrix.append(row)

    T = int(input())

    if R < 3 or C < 3:
        print(0)
        return

    count = 0

    for i in range(R - 2):
        for j in range(C - 2):
            temp = []
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    temp.append(matrix[x][y])

            temp.sort()
            median = temp[4]

            if median >= T:
                count += 1

    print(count)

solve()