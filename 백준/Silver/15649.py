# Silver3 / 260329
# 블로그 링크 : https://hakssi.tistory.com/32

import sys

n, m = map(int, sys.stdin.readline().split())

s = []
visited = [False] * (n + 1)
# Java의 StringBuilder 역할을 할 리스트
results = []

def dfs():
    if len(s) == m:
        results.append(" ".join(map(str, s)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            dfs()
            s.pop()
            visited[i] = False

dfs()

# 모든 탐색이 끝난 후, 쌓아둔 결과들을 줄바꿈(\n)으로 합쳐서 단 한 번만 출력
print("\n".join(results))