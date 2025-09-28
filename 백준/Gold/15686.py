"""
Gold 5
치킨 배달
문제 링크 : https://www.acmicpc.net/problem/15686
"""
import sys
from itertools import combinations
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    grid = []
    house_list = []
    chicken_shops = []

    for i in range(n): # 배열 구성
        row = list(map(int, input().split()))
        grid.append(row)

    for i in range(n): # 집과 치킨집 위치 확인
        for j in range(n):
            if grid[i][j] == 1:
                house_list.append([i, j])
            elif grid[i][j] == 2:
                chicken_shops.append([i, j])

    answer = sys.maxsize
    for selected_chickens in combinations(chicken_shops, m):
        total_distance = 0 # 각각의 조합마다 치킨거리 계산

        for house in house_list:
            min_distance = sys.maxsize
            for chicken in selected_chickens:
                d = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
                min_distance = d if min_distance > d else min_distance
            total_distance += min_distance

        answer = total_distance if answer > total_distance else answer

    print(answer)

solve()