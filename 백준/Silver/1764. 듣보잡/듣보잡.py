# 1764 듣보잡

N, M = map(int, input().split())
hear = [input() for _ in range(N)]
look = [input() for _ in range(M)]

hear_look = set(hear) & set(look)

print(len(hear_look))
for ix in sorted(list(hear_look)):
    print(ix)