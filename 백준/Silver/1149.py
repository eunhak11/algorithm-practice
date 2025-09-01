import sys

n = int(sys.stdin.readline().strip())
min_price = [[0 for _ in range(n)] for _ in range(3)]  # n번째 집일 때의 최소 비용

# price_table = [[0]*3]*n -> 얕은복사문제. grok 참고
price_table = [[0 for _ in range(3)] for _ in range(n)] # 얕은 복사 문제 방지

for i in range(n):
    # 입력 확인
    price_table[i][0], price_table[i][1], price_table[i][2] \
        = map(int, sys.stdin.readline().strip().split())

print(min_price)