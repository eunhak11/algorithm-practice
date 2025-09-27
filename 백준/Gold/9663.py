"""
Gold 4
N-Queen
문제 링크 : https://www.acmicpc.net/problem/9663
"""
import sys

def solve():
    n = int(sys.stdin.readline().rstrip())

    # 각 열, 대각선에 퀸이 있는지 체크하는 배열
    col = [False] * n
    diag1 = [False] * (2 * n - 1)  # row + col
    diag2 = [False] * (2 * n - 1)  # row - col + n - 1

    def rec(row):
        if row == n:
            return 1

        count = 0
        for c in range(n):
            if not col[c] and not diag1[row + c] and not diag2[row - c + n - 1]:
                col[c] = True
                diag1[row + c] = True
                diag2[row - c + n - 1] = True

                count += rec(row + 1)

                col[c] = False
                diag1[row + c] = False
                diag2[row - c + n - 1] = False

        return count

    print(rec(0))

solve()