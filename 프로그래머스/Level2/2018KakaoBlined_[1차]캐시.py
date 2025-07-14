"""
2018 KAKAO BLIND RECRUITMENT
[1차] 캐시
https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""

from collections import deque

def solution(cache_size, cities):

    answer = 0
    dq_cache = deque()

    if cache_size == 0:
        return len(cities) * 5

    else:
        for city in cities:
            city = city.upper()

            # hit
            if city in dq_cache:
                dq_cache.remove(city)
                answer += 1
            # miss
            else:
                if len(dq_cache) >= cache_size:
                    dq_cache.popleft()
                answer+=5

            dq_cache.append(city)

    return answer