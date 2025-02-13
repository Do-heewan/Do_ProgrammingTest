# 1946 신입 사원

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    people = []
    for _ in range(N):
        a, b = map(int, input().split())
        people.append((a, b))
    
    people.sort(key = lambda x : x[0]) # 성적이 낮은 순 정렬

    price = 1
    target = people[0][1] # 등수
    
    # 등수 비교
    for i in range(1, len(people)):
        if (target > people[i][1]): # 등수가 더 크다 -> 순위가 낮다 -> 성적도 낮고 순위도 낮다
            price += 1
            target = people[i][1]

    print(price)
