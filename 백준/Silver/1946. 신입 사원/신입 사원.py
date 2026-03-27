# 1946 신입사원

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    people = []
    for _ in range(N):
        people.append(list(map(int, input().split())))

    people.sort()

    cnt = 0
    curr_b = N+1
    for a, b in people:
        if b < curr_b:
            curr_b = b
            cnt += 1

    print(cnt)