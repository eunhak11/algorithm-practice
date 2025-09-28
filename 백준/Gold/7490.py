"""
Gold 5
0 만들기
문제 링크 : https://www.acmicpc.net/problem/7490
"""

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())

        results = []

        def backtrack(pos, expression):
            # 모든 숫자를 다 사용했을 때
            if pos == n:
                # 공백을 제거하고 계산
                calc_expr = expression.replace(' ', '')
                try:
                    if eval(calc_expr) == 0:
                        results.append(expression)
                except:
                    pass
                return

            # 다음 숫자
            next_num = str(pos + 1)

            # 3가지 연산자 시도: 공백, +, -
            backtrack(pos + 1, expression + ' ' + next_num)  # 공백
            backtrack(pos + 1, expression + '+' + next_num)  # 덧셈
            backtrack(pos + 1, expression + '-' + next_num)  # 뺄셈

        # 첫 번째 숫자 '1'부터 시작
        backtrack(1, '1')

        # 결과를 사전순으로 정렬하여 출력
        results.sort()
        for result in results:
            print(result)
        # 테스트 케이스 사이에 빈 줄
        print()

solve()
