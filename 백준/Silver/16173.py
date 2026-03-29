import sys

n = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(idx_x, idx_y):
    # 이미 탐색 한 적 있는 경우 > 도착 못하는 경우
    if idx_x >= n or idx_y >= n or visited[idx_x][idx_y]:
        return False

    if field[idx_x][idx_y] == -1:
        return True

    # 칸수로 계산 해야 하는 부분
    visited[idx_x][idx_y] = True
    jump = field[idx_x][idx_y]

    if jump==0: # 0이면 무한루프
        return False

    # 이렇게 하면 x,y를 둘다 끝까지 계산한다.
    # 아래처럼 하면 dfs_x가 True를 반환하는 순간 바로 종료.
    # dfs_x = dfs(idx_x+jump, idx_y)
    # dfs_y = dfs(idx_x, idx_y+jump)
    #
    # if dfs_x or dfs_y:
    #     return True

    if dfs(idx_x + jump, idx_y) or dfs(idx_x, idx_y + jump):
        return True

    return False

if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")