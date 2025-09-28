"""
Gold 5
치킨 배달
문제 링크 : https://www.acmicpc.net/problem/15686
"""
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    city = []
    for i in range(n):
        row = list(map(int, input().split()))
        city.append(row)



solve()