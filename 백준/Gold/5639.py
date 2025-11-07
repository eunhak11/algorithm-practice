"""
Gold 4
이진 검색 트리
문제 링크 : https://www.acmicpc.net/problem/5639

전위 순회(preorder) 결과가 주어졌을 때, 후위 순회(postorder) 결과를 출력하는 문제

전위 순회: 루트 -> 왼쪽 -> 오른쪽
후위 순회: 왼쪽 -> 오른쪽 -> 루트

이진 검색 트리 특성:
- 왼쪽 서브트리의 모든 노드 < 루트
- 오른쪽 서브트리의 모든 노드 > 루트
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def postorder(preorder_list):
    if not preorder_list:
        return

    # 전위 순회의 첫 번째 원소는 루트
    root = preorder_list[0]

    # 루트보다 큰 첫 번째 값의 인덱스를 찾음 (오른쪽 서브트리의 시작점)
    right_idx = len(preorder_list)
    for i in range(1, len(preorder_list)):
        if preorder_list[i] > root:
            right_idx = i
            break

    # 왼쪽 서브트리: preorder_list[1:right_idx]
    # 오른쪽 서브트리: preorder_list[right_idx:]
    postorder(preorder_list[1:right_idx])  # 왼쪽
    postorder(preorder_list[right_idx:])    # 오른쪽
    print(root)                             # 루트

# 입력 받기
preorder = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        preorder.append(int(line))
    except:
        break

# 후위 순회 출력
postorder(preorder)