# 1149 RGB 거리

import sys
input = sys.stdin.readline

N = int(input())

# 첫 번째 RGB
li = list(map(int, input().split()))

# 두 번째 RGB부터 더해가며 값을 비교
for _ in range(N-1):
    r, g, b = map(int, input().split())

    new_r = min(r + li[1], r + li[2])
    new_g = min(g + li[0], g + li[2])
    new_b = min(b + li[0], b + li[1])

    # 새로운 리스트로 저장
    li = [new_r, new_g, new_b]

print(min(li))