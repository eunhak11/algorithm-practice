import sys

n, k, c = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))
ans = float('inf')

def get_min_time():
    low = 1
    high = 10 ** 12
    res = high
    while low <= high:
        mid = (low + high) // 2
        total = 0
        for t in times:
            total += mid // t
        if total >= k:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

def dfs(remain_c, start):
    global ans
    current_res = get_min_time()
    if current_res < ans:
        ans = current_res

    if remain_c == 0:
        return

    for i in range(start, n):
        if times[i] > 1:
            times[i] -= 1
            dfs(remain_c - 1, i)
            times[i] += 1

dfs(c, 0)
print(int(ans))