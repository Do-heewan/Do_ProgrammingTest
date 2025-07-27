# 17404 RGB 거리

N = int(input())

INF = 1_000_000_000

first = list(map(int, input().split()))
dp_1 = [first[0], INF, INF]
dp_2 = [INF, first[1], INF]
dp_3 = [INF, INF, first[2]]

for _ in range(N-2):
    rgb = list(map(int, input().split()))
    dp_1 = [rgb[0] + min(dp_1[1:]), rgb[1] + min(dp_1[0], dp_1[2]), rgb[2] + min(dp_1[:2])]
    dp_2 = [rgb[0] + min(dp_2[1:]), rgb[1] + min(dp_2[0], dp_2[2]), rgb[2] + min(dp_2[:2])]
    dp_3 = [rgb[0] + min(dp_3[1:]), rgb[1] + min(dp_3[0], dp_3[2]), rgb[2] + min(dp_3[:2])]

last = list(map(int, input().split()))

dp_1 = [INF, last[1] + min(dp_1[0], dp_1[2]), last[2] + min(dp_1[:2])]
dp_2 = [last[0] + min(dp_2[1:]), INF, last[2] + min(dp_2[:2])]
dp_3 = [last[0] + min(dp_3[1:]), last[1] + min(dp_3[0], dp_3[2]), INF]

print(min(min(dp_1), min(dp_2), min(dp_3)))