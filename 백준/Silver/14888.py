"""
Silver1
연산자 끼워넣기
문제 링크 : https://www.acmicpc.net/problem/14888
"""
import sys

def solve():
    n = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    operators = list(map(int, sys.stdin.readline().split()))  # +, -, *, /

    max_result = float('-inf')
    min_result = float('inf')

    def backtrack(index, current_result, plus, minus, multiply, divide):
        nonlocal max_result, min_result

        # 모든 수를 다 사용했을 때
        if index == n:
            max_result = max(max_result, current_result)
            min_result = min(min_result, current_result)
            return

        # 덧셈 연산자가 남아있으면
        if plus > 0:
            backtrack(index + 1, current_result + numbers[index], plus - 1, minus, multiply, divide)

        # 뺄셈 연산자가 남아있으면
        if minus > 0:
            backtrack(index + 1, current_result - numbers[index], plus, minus - 1, multiply, divide)

        # 곱셈 연산자가 남아있으면
        if multiply > 0:
            backtrack(index + 1, current_result * numbers[index], plus, minus, multiply - 1, divide)

        # 나눗셈 연산자가 남아있으면
        if divide > 0:
            # 음수를 양수로 나눌 때 처리
            if current_result < 0:
                result = -(-current_result // numbers[index])
            else:
                result = current_result // numbers[index]
            backtrack(index + 1, result, plus, minus, multiply, divide - 1)

    # 첫 번째 수부터 시작 (index=1, 첫 번째 수는 이미 current_result에 포함)
    backtrack(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

    print(max_result)
    print(min_result)

solve()