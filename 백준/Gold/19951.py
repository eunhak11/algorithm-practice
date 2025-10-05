"""
Gold 5
태상이의 훈련소 생활
문제 링크 : https://www.acmicpc.net/problem/19951
"""
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    ground = list(map(int, input().split()))
    flag = [0 for _ in range(n+2)]

    for _ in range(m):
        a, b, k = map(int, input().split())
        flag[a-1] += k
        flag[b] -= k

    answer = [0 for i in range(n)]
    agg_sum = 0
    for i in range(n):
        agg_sum += flag[i]
        answer[i] = ground[i] + agg_sum

    for e in answer:
        print(e, end=" ")
solve()