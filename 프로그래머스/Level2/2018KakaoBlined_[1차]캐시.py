"""
2018 KAKAO BLIND RECRUITMENT
[1차] 캐시
문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17680
블로그 링크 :
"""

from collections import deque

def solution(cache_size, cities):

    answer = 0
    dq_cache = deque() # deque를 사용한 문제 풀이

    if cache_size == 0: # 캐시가 비어있는 경우 (miss)
        return len(cities) * 5 #

    else:
        # 대소문자를 구분하지 않기 때문에 모두 대문자로 변환해서 풀이 진행
        for city in cities:
            city = city.upper()

            # hit
            if city in dq_cache:
                # LRU이기 때문에 deque에서 지우고 맨 오른쪽에 다시 넣을 것이다.
                dq_cache.remove(city)
                answer += 1
            # miss
            else:
                # 캐시가 가득 차있는 경우는 LRU에 따라 가장 오랫동안 사용되지 않은(가장 왼쪽) 도시 삭제
                if len(dq_cache) >= cache_size:
                    dq_cache.popleft()
                answer+=5

            # deque 가장 오른쪽에 방금의 도시를 추가한다.
            dq_cache.append(city)

    return answer