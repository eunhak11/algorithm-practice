"""
Silver3
도키도키 간식드리미
문제 링크 : https://www.acmicpc.net/problem/12789
블로그 링크 :
"""

import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

stack = []
target = 1
i = 0

while target <= N:
    # 스택 맨 위가 찾는 번호면 간식 받기
    if stack and stack[-1] == target:
        stack.pop()
        target += 1
    # 대기줄에서 찾는 번호가 나오면 간식 받기
    elif i < N and line[i] == target:
        i += 1
        target += 1
    # 대기줄에 학생이 남아있으면 스택으로 이동
    elif i < N:
        stack.append(line[i])
        i += 1
    # 더 이상 진행할 수 없는 경우
    else:
        break

print("Nice" if target > N else "Sad")