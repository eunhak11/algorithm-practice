def solution(n, w, num):
    # 목표 상자의 좌표를 구하는 함수
    def get_coordinate(target):
        target -= 1  # w로 나누었을 때 나머지가 0~5가 되게 하기 위해
        y = target // w  # 몫을 통해 높이를 확인
        if y % 2 == 0:  # 짝수층인 경우 (왼쪽에서 오른쪽으로 증가)
            x = target % w
        else:  # 홀수층인 경우 (오른쪽에서 왼쪽으로 증가)
            x = w - target % w - 1
        return x, y

    num_x, num_y = get_coordinate(num)  # num의 좌표
    n_x, n_y = get_coordinate(n)  # n의 좌표

    answer = n_y - num_y + 1

    # 맨 윗층이 비어있는 경우를 찾아 1을 뺄 것이다.
    if n_y % 2 == 0:  # 짝수층인 경우
        if n_y > num_y and num_x > n_x:
            answer -= 1
    else:  # 홀수층인 경우
        if n_y > num_y and num_x < n_x:
            answer -= 1

    return answer