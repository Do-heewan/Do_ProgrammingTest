# 1149 RGB 거리

N = int(input())

# 첫 번째 RGB
li = list(map(int, input().split()))

for _ in range(N-1):
    r, g, b = map(int, input().split())

    new_r = min(r + li[1], r + li[2])
    new_g = min(g + li[0], g + li[2])
    new_b = min(b + li[0], b + li[1])

    li = [new_r, new_g, new_b]

    # print(li)

print(min(li))